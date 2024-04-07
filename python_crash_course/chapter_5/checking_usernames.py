current_users = ['Admin','bryAn','SEBas','neLly','Caty']
new_users = ['admin','bryan','x','y','z']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
        if new_user.lower() in current_users_lower:
            print('You need to enter a new username')
        else:
            print('Username is available')    

