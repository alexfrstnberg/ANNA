import os

def write_to_another_file(source, target, reversed=False):
    with open(os.path.join('L9', source)) as s:
        with open(os.path.join('L9', target), "w") as t:
            if reversed==False:
                for line in s:
                    t.write(line)
            else:
                for line in s.readlines()[::-1]:
                    t.write(line)


print('Writing source file content to thetarget file...')
write_to_another_file('9.2.source.txt', '9.2.target.txt')

print('Writing source file content to thetarget file in reversed order(lines)...')
write_to_another_file('9.2.source.txt', '9.2.target_reversed.txt', True)