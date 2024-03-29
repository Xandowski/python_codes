file = 'notes.txt'


class Error(Exception):
    pass


class InputError(Error):
    def __init__(self, message):
        self.message = message


def write_files(file):
    student_notes = get_students_notes()

    with open(file, 'a') as file:
        for student in student_notes:
            file.write(f'{student}: ')
            for x in range(0, 4):
                file.write(f'n{x + 1}={student_notes[student]["notes"][x]}, ')
            file.write(f'media={student_notes[student]["media"]}')
            file.write('\n')


def get_students_notes():
    students_notes = {}
    note = ''

    try:
        number_students = int(input('Digite a quantidade de alunos(as): '))
    except ValueError:
        print('Digite apenas numeros!')

    for x in range(1, number_students+1):
        name = input(f'Digite nome do {x}º aluno(a): ')
        notes = []

        for x in range(1, 5):
            try:
                note = float(input(f'Digite a {x}ª nota de {name}: '))

                if note > 10:
                    raise InputError('Nota não pode ser maior que 10.')
                elif note < 0:
                    raise InputError('Nota não pode ser menor que 0.')

            except ValueError:
                print('Digite apenas numeros!')
            except InputError as ex:
                print(ex)

            notes.append(note)

        average = students_average(notes)

        students_notes[f'{name}'] = {
            "notes": notes,
            "media": average
        }

    return students_notes


def students_average(notes):
    average = 0
    for student_note in notes:
        average += student_note
    return average / len(notes)


write_files(file)
