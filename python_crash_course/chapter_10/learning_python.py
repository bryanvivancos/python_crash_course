from pathlib import Path

path = Path('C:/Users/BRYAN/workspace/python_crash_course/python_crash_course/chapter_10/learning_python.txt')
contents = path.read_text()
print('Reading lines of the text:')
print(contents)

print('\nStoring the lines in the list:')
lines = contents.splitlines()
for line in lines:
    print(line)