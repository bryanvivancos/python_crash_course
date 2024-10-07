from pathlib import Path

path = Path('C:/Users/BRYAN/workspace/python_crash_course/python_crash_course/chapter_10/guest.txt')
user_name = input('Please input your name: ')
contents = user_name
path.write_text(contents)