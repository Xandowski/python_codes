animals = ['cachorro', 'gato', 'peixe']

animals_obj = {
    'cachorro': lambda animals: len(animals[0]),
    'gato': lambda animals: len(animals[1]),
    'peixe': lambda animals: len(animals[2]),
}

print(animals_obj['cachorro'](animals))
