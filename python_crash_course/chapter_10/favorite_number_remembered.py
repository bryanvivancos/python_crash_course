#program that prompts for the user's favorite number and then read it to prints it
from pathlib import Path
import json

path = Path('C:\\Users\\BRYAN\\workspace\\python_crash_course\\python_crash_course\\chapter_10\\files_json\\fav_number_remembered.json')

if path.exists():
    content = path.read_text()
    number = json.loads(content)
    print(f"I know your favorite number! It's {number}")
else: 
    number = input('Whats your favorite number?: ')
    content = json.dumps(number)
    path.write_text(content)
    print('Thanks for answer')