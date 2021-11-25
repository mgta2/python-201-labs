# Add the code for the file counter script that you wrote in the course.

import pathlib

desktop = pathlib.Path("C:\\Users\Matthew\Desktop")
my_dict = {}

# Create dictionary to see frequency of each file type.

for filepath in desktop.iterdir():
    suf = filepath.suffix
    if suf in my_dict.keys():
        my_dict[suf] += 1
    else:
        my_dict[suf] = 1

print(my_dict)

# List the file types when more than 15 files exist on desktop.

bigkey_list = []

for key, value in my_dict.items():
    if value > 15:
        # Make new folder to put these frequent file types into.
        new_path = pathlib.Path(f"C:\\Users\Matthew\Desktop\Folder_for_{key[1:]}")
        new_path.mkdir(exist_ok=True)
        bigkey_list.append(key)

# For each file with common file type, move it into this new folder.

for filepath in desktop.iterdir():
    if filepath.suffix in bigkey_list:
        our_path = pathlib.Path(f"C:\\Users\Matthew\Desktop\Folder_for_{filepath.suffix[1:]}\{filepath.name}")
        filepath.replace(our_path)

# Program tested for .xlsx file types and it works as expected.