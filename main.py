import json
import os
import sys


def parse_and_create_files(mode):
    """
    Parses data.json and creates a .java file for each entry.
    """
    json_file_path = 'data/data.json'
    os.makedirs("output", exist_ok=True)

    if not os.path.exists(json_file_path):
        print(f"Error: File not found at {json_file_path}")
        return

    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    start_id = 1
    for i, item in enumerate(data):
        file_id = start_id + i
        file_name = f"S{file_id}.java"
        
        if mode in item:
            code_content = item[mode]
            
            try:
                with open("output/" + file_name, 'w', encoding='utf-8') as java_file:
                    java_file.write(code_content)
                print(f"Created {file_name}")
            except IOError as e:
                print(f"Error writing to file {file_name}: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <mode>")
        print("Where <mode> is either 'buggy_code' or 'fixed_code'")
        print("Example: python3 main.py buggy_code")
        sys.exit(1)
    
    mode = sys.argv[1]
    if mode not in ["buggy_code", "fixed_code"]:
        print(f"Error: Invalid mode '{mode}'. Please use 'buggy_code' or 'fixed_code'.")
        sys.exit(1)

    parse_and_create_files(mode)