import re
import os

class MarkdownEditor:
    def __init__(self, filepath: str):
        self.filepath = filepath
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            self.content = f.read()

    def update_section(self, marker_start: str, marker_end: str, new_content: str) -> bool:
        """
        Update content between two markers.
        """
        pattern = re.escape(marker_start) + r"(.*?)" + re.escape(marker_end)
        
        # Check if markers exist
        if not re.search(pattern, self.content, re.DOTALL):
            print(f"Warning: Markers {marker_start}...{marker_end} not found in {self.filepath}")
            return False
            
        replacement = f"{marker_start}{new_content}{marker_end}"
        self.content = re.sub(pattern, replacement, self.content, flags=re.DOTALL)
        return True

    def save(self):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            f.write(self.content)

    @staticmethod
    def generate_download_table(mirrors_data: list, version: str) -> str:
        """
        Generate a Markdown table for download links.
        """
        header = "| 下载源 | 版本 | 说明 | 状态 |\n|--------|------|------|------|"
        rows = []
        
        for mirror in mirrors_data:
            name = mirror['name']
            url = mirror['url']
            status = "✅" if mirror.get('status', True) else "❌"
            note = "[下载链接]({})".format(url)
            
            rows.append(f"| {name} | {version} | {note} | {status} |")
            
        return header + "\n" + "\n".join(rows)

    def update_link(self, marker_start: str, marker_end: str, new_url: str) -> bool:
        """
        Update a URL between markers.
        """
        return self.update_section(marker_start, marker_end, new_url)
