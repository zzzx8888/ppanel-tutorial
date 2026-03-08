# PPanel Tutorial Maintenance Tool

This directory contains tools to automate the maintenance of the ppanel-tutorial documentation.

## Features
- Fetches the latest release information from GitHub.
- Generates mirror download links.
- Verifies link availability.
- Updates Markdown files with new versions, filenames, and download tables.

## Usage

1. Install dependencies:
   ```bash
   pip install -r maintenance/requirements.txt
   ```

2. Configure `maintenance/config.yaml`.

3. Run the script:
   ```bash
   python maintenance/main.py
   ```
