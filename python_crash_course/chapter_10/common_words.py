from pathlib import Path

file = 'peter_pan.txt'
path = Path(f'C:\\Users\\BRYAN\\workspace\\python_crash_course\\python_crash_course\\chapter_10\\{file}')

words = ['the','then','there','the ']

for word in words:
    try:
        content = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f'File "{file}" is not found, please check the root')
    else:
        print(f'In {file} we can find the word "{word}" {content.lower().count(word)} times')