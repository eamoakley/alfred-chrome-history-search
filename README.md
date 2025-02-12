# Alfred Workflow: Chrome History Search

## Overview

This Alfred workflow allows you to search your Google Chrome browser history directly from Alfred. You can trigger the search using a keyword or hotkey, and the results will update dynamically as you type. Selecting an item will open the corresponding page in a new Chrome tab, and holding the `Cmd` key while selecting will copy the URL to the clipboard.

## How It Works

1. **Trigger**: Use the keyword `hist` (or your chosen keyword) to activate the workflow.
2. **Search**: As you type, the workflow queries your Chrome history database for matching titles or URLs.
3. **Results**: The results are displayed in Alfred, showing the page title and URL.
4. **Actions**:
   - **Open in Chrome**: Select an item to open it in a new tab.
   - **Copy URL**: Hold `Cmd` while selecting to copy the URL to the clipboard.

## Configuration

### Prerequisites
- **Chrome**: Ensure Chrome is installed on your system.
- **Python**: Ensure Python is installed on your system. The script uses Python to query the database.
- **Alfred Powerpack**: This workflow requires the Alfred Powerpack for advanced features like Script Filters.

### Setup Instructions

1. **Database Path**: The script assumes the default path for Chrome's history database. If you use a different profile or have a custom setup, update the `history_db` variable in the script to point to the correct location.
   
2. **Script Filter**: Ensure the Script Filter in Alfred is configured to pass the query string to the script. Set the "Argument" field to `{query}`.

3. **Permissions**: Ensure the script has permission to read from the Chrome history database. You may need to adjust your system's privacy settings to allow this.

4. **Temporary Directory**: The script creates a temporary copy of the database to avoid lock issues. Ensure your system allows the creation of temporary files.

### Cross-Machine Setup

- **Database Path**: Verify the path to the Chrome history database on each machine, as it may vary based on user profiles or operating system versions.
- **Python Version**: Ensure the correct version of Python is installed and accessible on each machine.
- **Alfred Version**: Make sure Alfred and the Powerpack are installed and up-to-date on each machine.

## Copyright and Credit

- **Author**: Eric Moakley
- **Year**: 2025
- **License**: This workflow is provided "as-is" without warranty of any kind. You are free to use and modify it for personal use.
- **Acknowledgments**: This workflow was inspired by the need for efficient access to browser history and leverages the power of Alfred and Python for seamless integration.