import os
from collections import OrderedDict

def print_file(name):
    print('File ' + name + ':')
    with open(name, 'r') as f:
        data = f.read()
        print(data)

def write_to_file(name='random.txt', text='no matter what', mode='a'):
    with open(name, mode) as f:
        data = f.write(('\n' if os.stat(name).st_size !=0 else '') + text)


def find_in_file(name, seq):
    with open(name, 'r') as f:
        content = f.read()
        try: print(seq, 'found at the position', content.index(seq))
        except ValueError as err: print('"',seq,'" ',err, sep='')

def sorting(source_name, path_name='sorted.txt'):
    data = {}
    with open(source_name, 'r') as f:
        for item in f.readlines():
            if item != '\n':
                key, value = item.strip().split(':')
                data[key] = int(value)

    data = OrderedDict(sorted(data.items(), key=lambda x:x[1], reverse=True))

    with open(path_name, 'w') as f:
        for key, value in data.items():
            f.write('{}: {}\n'.format(key, value))

print('Printinting file:\n')
print_file('students.txt')

print('Writing to file...(check the folder)\n')
write_to_file('file.txt', 'written text', mode='w')

print('Append text to file...(check the folder)\n')
write_to_file('file.txt', 'added text', mode='a')

print('Searching in file:')
find_in_file('students.txt', 'Max')

print('\nSorting students by average mark...(check folder)')
sorting('students.txt')







