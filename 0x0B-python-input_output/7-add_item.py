#!/usr/bin/python3
"""Playing with JSON files."""
import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


fileJson = 'add_item.json'
listJson = []

if os.path.exists(fileJson) and os.path.getsize(fileJson) > 0:
    listJson = load_from_json_file(fileJson)
if len(sys.argv) > 1:
    for args in sys.argv[1:]:
        listJson.append(args)
save_to_json_file(listJson, fileJson)
