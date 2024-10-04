def buildProfile(first,last,**user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    
    return user_info

myProfile = buildProfile('Bryan', 'Vivanco', edad = 26, trabajo = 'Ingeniero Software')
print(myProfile)