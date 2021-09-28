n = int(input())

fib_list = []

for i in range(n):
    if i < 2:
        fib_list.append(str(i))
    else:
        temp = int(fib_list[-1])
        temp2 = int(fib_list[-2])
        fib_list.append(str(temp + temp2))

fib_string = ' '.join(fib_list)
print(fib_string)
