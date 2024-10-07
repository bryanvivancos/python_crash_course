from pathlib import Path

filenames = ['cats.txt','dogs.txt']

for file in filenames:
    path = Path(f'C:\\Users\\BRYAN\\workspace\\python_crash_course\\python_crash_course\\chapter_10\\{file}')
    try: 
        content = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f'File "{file}" is not found, please check the root')
    else:
        print(f'{file}: ')
        lines = content.splitlines()
        for line in lines:
            print(f' -{line}')