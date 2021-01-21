import pandas as pd

f = open("C:/Users/xandy/Documents/txtFiles/enotest.txt", "r")
lines = f.readlines()
f.close()

keep = []

# for line in lines:
#     if line == 1:
#         line = "test"

#     line = line.replace(",", ".")
#     line = line.replace("got server runtimes", "")
#     line = line.replace("*", "")
#     if not line.isspace():
#         keep.append(line)

for line in range(len(lines)):
    if line == 1:
        lines[line] = lines[line].strip()

    lines[line] = lines[line].replace(",", ".")
    lines[line] = lines[line].replace("got server runtimes", "")
    lines[line] = lines[line].replace("*", "")
    lines[line] = lines[line].replace("  ", " ")

    if line == 1:
        lines[line] = lines[line].lstrip()

    if not lines[line].isspace():
        keep.append(lines[line])


f2 = open("C:/Users/xandy/Documents/txtFiles/enotest2.txt", "a")
f2.writelines(keep)
f2.close()

df = pd.read_csv(
    "C:/Users/xandy/Documents/txtFiles/enotest2.txt", sep="\s+", header=None)
df.to_excel("C:/Users/xandy/Documents/txtFiles/newF.xlsx", "sheet1")
