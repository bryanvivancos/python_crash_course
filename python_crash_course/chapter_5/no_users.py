username = []

if username:
    for user in username:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {user}, thank you for logging again.')
else:
    print('We need to find some users')