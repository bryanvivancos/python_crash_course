from pathlib import Path
import json

def get_stored_userdata(path):
    """Get stored userdata if available."""
    if path.exists():
        contents = path.read_text()
        user_data = json.loads(contents)
        return user_data
    else:
        return None

def get_new_userdata(path):
    """Prompt for a new userdata."""
    user_firstname = input("What is your first name? ")
    user_lastname = input("What is your last name? ")
    user_phone = input("What is your phone? ")
    
    user_data = {
        'firstname':user_firstname,
        'lastname':user_lastname,
        'phone':user_phone
    }

    contents = json.dumps(user_data)
    path.write_text(contents)
    return user_data

def greet_user():
    """Greet the user by name."""
    path = Path('C:\\Users\\BRYAN\\workspace\\python_crash_course\\python_crash_course\\chapter_10\\files_json\\user_dictionary.json')
    user_data = get_stored_userdata(path)
    if user_data:
        print(f"Welcome back, {user_data['firstname']} {user_data['lastname']}!")
    else:
        user_data = get_new_userdata(path)
        print(f"We'll remember you when you come back, {user_data['firstname']} {user_data['lastname']}!")

greet_user()