## Steps to use:

1. Download `label_app.html`
2. Copy the values from the line starting with `const PAIRS = ` to `data/data.json`
3. Run the script with `python main.py`
    NOTE: The `buggy_code` value from each element in `data.json` will be written to `output/<id>.java`
4. Stage the files in output/
5. Update the `MODE` in the script to `fixed_code` and run the script again

You should now be able to see the diff in each java file.