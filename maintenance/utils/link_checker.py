import requests
from typing import List, Dict, Tuple

class LinkChecker:
    def __init__(self, timeout: int = 5):
        self.timeout = timeout
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    def check_url(self, url: str) -> bool:
        """
        Check if a URL is reachable via HEAD request.
        Returns True if status code is 200-399.
        """
        try:
            response = requests.head(url, headers=self.headers, timeout=self.timeout, allow_redirects=True)
            return 200 <= response.status_code < 400
        except requests.RequestException:
            return False

    def generate_and_check(self, original_url: str, mirrors_config: List[Dict]) -> List[Dict]:
        """
        Generate mirror links and check their status.
        
        Args:
            original_url: The official download URL
            mirrors_config: List of mirror configurations from config.yaml
            
        Returns:
            List of dicts with keys: name, url, status (bool)
        """
        results = []
        
        for mirror in mirrors_config:
            template = mirror.get("url_template", "{url}")
            mirror_url = template.replace("{url}", original_url)
            
            is_valid = True
            if mirror.get("check_availability", False):
                is_valid = self.check_url(mirror_url)
            
            results.append({
                "name": mirror["name"],
                "url": mirror_url,
                "status": is_valid
            })
            
        return results
