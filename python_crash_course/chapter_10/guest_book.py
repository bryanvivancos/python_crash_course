from pathlib import Path

path = Path('C:/Users/BRYAN/workspace/python_crash_course/python_crash_course/chapter_10/guest_book.txt')

prompt = '\nHi, please entry your name'
prompt += '\n(Enter "q" if you want to break): '

guest_names = []
while (True):  
    name = input(prompt)
    if name == 'q':
        break
    print(f'Thanks {name}')
    guest_names.append(name)

# Build a string where "\n" is added after each name.
guests = ''
for name in guest_names:
    guests += f'{name}\n'

path.write_text(guests)