# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere.

from pathlib import Path

desktop = Path("C:\\Users\Matthew\Desktop")
target = desktop.joinpath("filecounts.csv")

my_dict = {}
for filepath in desktop.iterdir():
    suf = filepath.suffix
    if suf in my_dict.keys():
        my_dict[suf] += 1
    else:
        my_dict[suf] = 1

data = []

for value in my_dict.values():
    data.append(value)

target.write_text(str(data))
print(target.read_text())