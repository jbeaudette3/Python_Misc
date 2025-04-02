import nbformat

def count_code_lines(notebook_path):
    with open(notebook_path, 'r') as f:
        nb = nbformat.read(f, as_version=4)
    code_lines = 0
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            code_lines += len(cell['source'].splitlines())
    return code_lines

print("Number of code lines:", count_code_lines('./filename.ipynb'))
