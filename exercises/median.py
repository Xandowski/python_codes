array1 = input("Digite um ou mais numeros, separados por espaçoss. Ex: 1 2 50..: ")
array2 = f'{array1} {input("Digite um ou mais numeros, separados por espaçoss. Ex: 1 2 50..: ")}'

array2 = sorted(list(map(int, array2.split())))

print(array2)

if len(array2) % 2 == 0:
    median = len(array2) / 2
    median2 = median - 1
    print(f"A mediana são {array2[int(median2)]} e {array2[int(median)]}")

else:
    median = int((len(array2) - 1) / 2)
    print(f"A mediana é {array2[int(median)]}")


array1 = [1, 5, 5, 9, 3, 6, 4]
array2 = [9, 4, 7, 5, 5, 1, 2]
array3 = []

for i in array1:
    for j in array2:
        if i < j:
            array3.append(i)
