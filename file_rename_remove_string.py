'''
This script is used to remove a specified string from files within a directory
Example:
Current Filename: 123456 - starting data.xlsx
New Filename: 123456.xlsx
'''
import os

path = r'C:\path\to\directory'
string_to_remove = ' - this will be removed'

files = os.listdir(path)

for f in files:
  if string_to_remove in f:
    idx = f.find(string_to_remove)
    ext = os.path.splitext(f)[-1]
    new_f = f'{f[:idx]}{ext}'

    old_path = os.path.join(path, f)
    new_path = os.path.join(path, new_f)

    os.rename(old_path, new_path)
