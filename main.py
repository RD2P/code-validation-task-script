import json
import os


# 1. First run with MODE = "buggy_code" to create files with buggy code.
# 2. Stage output
# 3. Set to MODE = "fixed_code" to create files with fixed code.
MODE = "buggy_code" 

def parse_and_create_files():
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

    start_id = 50001
    for i, item in enumerate(data):
        file_id = start_id + i
        file_name = f"{file_id}.java"
        
        if MODE in item:
            code_content = item[MODE]
            
            try:
                with open("output/" + file_name, 'w', encoding='utf-8') as java_file:
                    java_file.write(code_content)
                print(f"Created {file_name}")
            except IOError as e:
                print(f"Error writing to file {file_name}: {e}")

if __name__ == '__main__':
    parse_and_create_files()