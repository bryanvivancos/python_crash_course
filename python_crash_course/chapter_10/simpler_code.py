from pathlib import Path

#simpler_code_file_reader
path = Path('C:/Users/BRYAN/workspace/python_crash_course/python_crash_course/chapter_10/pi_digits.txt')
contents = path.read_text()

for line in contents.splitlines():
    print(line)
    
#simpler_code_pi_string
path = Path('C:/Users/BRYAN/workspace/python_crash_course/python_crash_course/chapter_10/pi_million_digits.txt')
contents = path.read_text()

pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

#simpler_code_pi_birthday
path = Path('C:/Users/BRYAN/workspace/python_crash_course/python_crash_course/chapter_10/pi_million_digits.txt')
contents = path.read_text()

pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")