#program that prompts for the user's favorite number
from pathlib import Path
import json

path = Path('C:\\Users\\BRYAN\\workspace\\python_crash_course\\python_crash_course\\chapter_10\\files_json\\fav_number.json')
number = input('Whats your favorite number?: ')
content = json.dumps(number)
path.write_text(content)
print('Thanks for answer')