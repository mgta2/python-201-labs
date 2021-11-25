# Adapt your file counter script so that it records more different file types
# in your CSV file. Remember that the format of your output needs to be
# consistent across multiple runs of your script. This means you'll need to
# make a compromise and choose which file types you want to record beforehand.

from pathlib import Path

desktop = Path("C:\\Users\Matthew\Desktop")
target = desktop.joinpath("filecounts.csv")
file_types = ["", ".pdf", ".docx", ".txt", ".png"]

my_dict = {"": 0, ".pdf": 0, ".docx": 0, ".txt": 0, ".png": 0}
for filepath in desktop.iterdir():
    suf = filepath.suffix
    if suf in file_types:
        if suf in my_dict.keys():
            my_dict[suf] += 1
        else:
            my_dict[suf] = 1

data = ""
for i in range(0,len(file_types)):
    data += f"{my_dict[file_types[i]]},"

target.write_text(data)
print(target.read_text())