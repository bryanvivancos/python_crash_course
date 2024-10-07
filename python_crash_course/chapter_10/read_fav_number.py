#Reading the value and prints it
from pathlib import Path
import json

path = Path('C:\\Users\\BRYAN\\workspace\\python_crash_course\\python_crash_course\\chapter_10\\files_json\\fav_number.json')
content = path.read_text()
number = json.loads(content)
print(f"I know your favorite number! It's {number}")