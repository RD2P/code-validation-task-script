## How to Use

This project includes an automation script to streamline the process of generating and comparing "buggy" and "fixed" versions of the code snippets.

### Automated Workflow
1. Download `label_app.html`

2. Copy the values from the line starting with `const PAIRS = ` to `data/data.json`

3.  **Ensure the script executable:**
    ```bash
    chmod +x run_all.sh
    ```

4.  **Run the automation script:**
    Execute the script from the root of the project directory.
    ```bash
    ./run_all.sh
    ```

The `run_all.sh` script performs the following sequence of actions:

1.  **Generates Buggy Code:** It runs `python3 main.py buggy_code`, which creates a `.java` file in the `output/` directory for each code snippet's "buggy" version.
2.  **Stages Changes:** It executes `git add .` to stage the newly created buggy files.
3.  **Generates Fixed Code:** It then runs `python3 main.py fixed_code`, which overwrites the existing files with the "fixed" versions of the code.

After the script completes, you can easily view the differences between the buggy and fixed versions of each file using standard Git commands.


### Viewing the Diffs

To see the changes for all files, run:
```bash
git diff
```

To see the changes for a specific file:
```bash
git diff output/S1.java
```

### Cleaning output/ directory

To clean the output, run the `clean.sh` script:
```bash
./clean.sh
```

## Manual steps:

1. Run the script with 
    
    ```bash
    python main.py buggy_code
    ```

    **NOTE**: The `buggy_code` value from each element in `data.json` will be written to `output/<id>.java`

2. Stage the files in output/

    ```bash
    git add output/
    ```

3. Run the script again with 
    ```bash
    python main.py fixed_code`
    ```

You should now be able to see the diff in each java file.