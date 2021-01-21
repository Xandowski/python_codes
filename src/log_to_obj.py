import pandas as pd
f = open("C:/Users/xandy/Documents/txtFiles/enotest.txt", "r").read()

# print(f)
# lines = f.readlines()

rawLog = f
rawLog = rawLog.replace('**', '')
sections = rawLog.split('*')
sectionsFinal = []
for section in sections:
    if len(section) > 1:
        sectionsFinal.append(section)

inicioDaExecucao = sectionsFinal[0]
print("inicioDaExecucao->", inicioDaExecucao)

allSectionObj = []

alpha = 0
tempSectionObj = {}
for section in sectionsFinal[1::]:

    if alpha == 0:
        tempSectionObj["nome"] = section
        alpha += 1
    elif alpha == 1:
        tempSectionObj["runtimes"] = section
        alpha += 1
    else:
        tempSectionObj["table"] = section
        allSectionObj.append(tempSectionObj)
        alpha = 0
        tempSectionObj = {}


def treat_section_table(table):
    table = table.split('\n')
    tableWithoutBlankLines = []
    for line in table:
        if len(line) > 0:
            tableWithoutBlankLines.append(line)

    columns = tableWithoutBlankLines[0].replace(
        "  ", "--").replace("--", "-").split('-')
    columnsFinal = []
    for col in columns:
        if len(col) > 0:
            columnsFinal.append(col)

    print(len(columnsFinal))

    tableObj = {}

    for columnIndex, column in enumerate(columnsFinal):
        allValues = []
        for line in tableWithoutBlankLines[1::]:
            values = line.replace("  ", "--").replace("--", "-").split('-')
            valuesFinal = []
            for value in values:
                if len(value) > 0:
                    valuesFinal.append(value)
            allValues.append(valuesFinal[columnIndex])
        tableObj[column] = allValues

    return tableObj


tableSection1 = treat_section_table(allSectionObj[0]["table"])

print(tableSection1)
df = pd.DataFrame(tableSection1, columns=tableSection1.keys())
logs = df.to_csv()
f2 = open("C:/Users/xandy/Documents/txtFiles/enotest2.txt", "a")

f2.writelines(logs)
f2.close()
df = pd.read_csv(
    "C:/Users/xandy/Documents/txtFiles/enotest2.txt", sep=",", header=None, encoding='ISO-8859-1')
df.to_excel("C:/Users/xandy/Documents/txtFiles/newFile.xlsx", "sheet1")
print(df)

# cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
#     'Price': [22000,25000,27000,35000]
#     }

# df = pd.DataFrame(cars, columns = ['Brand', 'Price'])
