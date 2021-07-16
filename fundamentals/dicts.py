c = {1, 2, 3, 4}
print(f'c: {c}')
c.add(5)
print(f'add: {c} 5 added')
c.remove(2)
print(f'discard: {c} 2 removed')

c1 = {1, 2, 3, 4, 5}
c2 = {5, 6, 7, 8}
print(f'\nc1: {c1}')
print(f'c2: {c2}')
c_union = c1.union(c2)
print(f'União: {c_union}')

c_intersection = c1.intersection(c2)
print(f'Intersecção: {c_intersection}')

c_difference = c1.difference(c2)
print(f'Diferença: {c_difference}')

c_sym_diff = c1.symmetric_difference(c2)
print(f'Diferença simétrica: {c_sym_diff}')

c3 = {1, 2, 3}
c4 = {1, 2, 3, 4, 5}

c_subset = c3.issubset(c4)
print(f'\nsubset: {c_subset}')

c_superset = c4.issuperset(c3)
print(f'superset: {c_superset}')

lista = ['cachorro', 'gato', 'gato', 'elefante']
c_animals = set(lista)
print(c_animals)
