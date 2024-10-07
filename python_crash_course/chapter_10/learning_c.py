from pathlib import Path

path = Path('C:/Users/BRYAN/workspace/python_crash_course/python_crash_course/chapter_10/learning_python.txt')
contents = path.read_text()
print('Reading lines of the text:')
print(contents)

print('\nReplacing the word "Python" to "C" in the list:')
lines = contents.splitlines()
word = 'Python'
for line in lines:
    line = line.replace(word,'C')
    print(line)