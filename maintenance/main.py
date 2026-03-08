import yaml
import os
import sys
import datetime
from typing import Dict, Any

# Add the current directory to sys.path to make imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.github_client import GitHubClient
from utils.link_checker import LinkChecker
from utils.markdown_editor import MarkdownEditor

def load_config(config_path: str) -> Dict[str, Any]:
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_dir, 'maintenance', 'config.yaml')
    
    print(f"Loading config from {config_path}")
    config = load_config(config_path)
    
    github = GitHubClient(token=os.environ.get("GITHUB_TOKEN"))
    checker = LinkChecker()
    
    for app in config.get('apps', []):
        print(f"Processing {app['name']} ({app['repo']})...")
        
        # 1. Fetch Release Info
        release = github.get_latest_release(
            repo=app['repo'],
            include_prerelease=app.get('prerelease', False),
            asset_filter=app.get('asset_filter', '')
        )
        
        if not release:
            print(f"❌ Failed to fetch release for {app['name']}")
            continue
            
        print(f"✅ Found version: {release['version']}")
        print(f"   Asset: {release.get('filename', 'N/A')}")
        
        # 2. Generate and Check Links
        original_url = release.get('asset_url')
        if not original_url:
            print("❌ No asset URL found, skipping link generation.")
            continue
            
        mirrors_data = checker.generate_and_check(original_url, config.get('mirrors', []))
        
        # 3. Update Target Files
        for target in app.get('target_files', []):
            file_path = os.path.join(base_dir, target['path'])
            print(f"   Updating {target['path']}...")
            
            try:
                editor = MarkdownEditor(file_path)
                markers = target.get('markers', {})
                
                # Update Version
                if 'version' in markers:
                    start, end = markers['version'].split('{}')
                    editor.update_section(start, end, release['version'])
                    
                # Update Filename
                if 'filename' in markers and 'filename' in release:
                    start, end = markers['filename'].split('{}')
                    editor.update_section(start, end, release['filename'])
                
                # Update Download Table
                if 'download_table' in markers:
                    start, end = markers['download_table'].split('{}')
                    # Generate table content
                    table_content = "\n" + editor.generate_download_table(mirrors_data, release['version']) + "\n"
                    # Note: The marker definition in config might include newlines, handled by split
                    # Actually, let's look at config: "<!-- ... -->\n{}\n<!-- ... -->"
                    # So start is "<!-- ... -->\n", end is "\n<!-- ... -->"
                    # We pass the table content which is the middle part.
                    editor.update_section(start, end, table_content)

                # Update Specific Link (new feature)
                if 'link' in markers:
                    # Expecting a list of {marker: "...", type: "mirror_index/original"} or just update original if simple
                    # But config.yaml structure is flexible. Let's say markers['link'] is "<!-- LINK_START -->{}<!-- LINK_END -->"
                    # This will update ONE link with the main asset URL.
                    # If we need multiple links (e.g. mirrors), we need a better config structure.
                    # For now, let's support updating the main asset URL.
                    start, end = markers['link'].split('{}')
                    editor.update_link(start, end, original_url)

                # Update Last Updated Time
                if 'last_updated' in markers:
                    start, end = markers['last_updated'].split('{}')
                    today = datetime.datetime.now().strftime("%Y-%m-%d")
                    editor.update_section(start, end, today)
                
                editor.save()
                print(f"   ✅ Updated {target['path']}")
                
            except Exception as e:
                print(f"   ❌ Failed to update {target['path']}: {e}")

if __name__ == "__main__":
    main()
