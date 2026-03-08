import requests
import re
from typing import Optional, Dict, Any

class GitHubClient:
    def __init__(self, token: Optional[str] = None):
        self.base_url = "https://api.github.com"
        self.headers = {
            "Accept": "application/vnd.github.v3+json"
        }
        if token:
            self.headers["Authorization"] = f"token {token}"

    def get_latest_release(self, repo: str, include_prerelease: bool = False, asset_filter: str = "") -> Optional[Dict[str, Any]]:
        """
        Get the latest release info for a repository.
        
        Args:
            repo: "owner/repo"
            include_prerelease: Whether to consider prereleases
            asset_filter: Regex or substring to match asset name
            
        Returns:
            Dict containing version, published_at, asset_url, filename, or None if not found
        """
        try:
            url = f"{self.base_url}/repos/{repo}/releases"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            releases = response.json()
            
            if not releases:
                return None
                
            target_release = None
            
            if include_prerelease:
                # Releases are usually sorted by date desc, so take the first one
                target_release = releases[0]
            else:
                # Find first non-prerelease
                for release in releases:
                    if not release.get("prerelease", False):
                        target_release = release
                        break
            
            if not target_release:
                return None
                
            # Find matching asset
            target_asset = None
            if asset_filter:
                for asset in target_release.get("assets", []):
                    if re.search(asset_filter, asset["name"], re.IGNORECASE):
                        target_asset = asset
                        break
            else:
                # If no filter, take the first asset? Or maybe just return release info without asset
                if target_release.get("assets"):
                    target_asset = target_release["assets"][0]
            
            result = {
                "version": target_release["tag_name"],
                "published_at": target_release["published_at"].split("T")[0], # YYYY-MM-DD
                "html_url": target_release["html_url"]
            }
            
            if target_asset:
                result["asset_url"] = target_asset["browser_download_url"]
                result["filename"] = target_asset["name"]
                result["size"] = target_asset["size"]
            
            return result
            
        except Exception as e:
            print(f"Error fetching release for {repo}: {e}")
            return None
