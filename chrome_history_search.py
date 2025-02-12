import sqlite3
import os
import json
import sys
import shutil
import tempfile

# Path to Chrome's history database
history_db = os.path.expanduser('~/Library/Application Support/Google/Chrome/Default/History')

# Create a temporary copy of the database to avoid lock issues
temp_dir = tempfile.mkdtemp()
temp_db = os.path.join(temp_dir, 'History')
shutil.copy2(history_db, temp_db)

# Connect to the copied database
conn = sqlite3.connect(temp_db)
cursor = conn.cursor()

# Get the search query from Alfred
query = sys.argv[1] if len(sys.argv) > 1 else ''

# Determine the number of items to fetch
num_items = 100

# Query to fetch history with search filter
cursor.execute(f"""
    SELECT url, title 
    FROM urls 
    WHERE title LIKE ? OR url LIKE ?
    ORDER BY last_visit_time DESC 
    LIMIT {num_items}
""", (f'%{query}%', f'%{query}%'))

# Fetch results
results = cursor.fetchall()

# Close the connection
conn.close()

# Remove the temporary database
shutil.rmtree(temp_dir)

# Format results for Alfred
items = []
for url, title in results:
    items.append({
        "title": title,
        "subtitle": url,
        "arg": url,
        "mods": {
            "cmd": {
                "valid": True,
                "arg": url,
                "subtitle": "Copy URL to clipboard"
            }
        }
    })

# Output results in JSON format
print(json.dumps({"items": items})) 