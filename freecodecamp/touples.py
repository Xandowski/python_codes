d = {'a':10, 'b': 1, 'c': 22}
tmp = list()
for key, value in d.items():
    tmp.append( (value, key) )

print(tmp)
print('----')
print(sorted([ (v, k) for k, v in d.items()], reverse=True))
