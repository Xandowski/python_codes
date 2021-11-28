N = int(input())

persons = list(map(int, input().split()))
print(persons)
lowest = min(persons)
print(lowest)
print(persons.index(lowest) + 1)
