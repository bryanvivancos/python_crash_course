def make_shirt(size,text):
    print(f"You ordered a '{size}' size Shirt with the text '{text}'")
    
def buildProfile(first,last,**user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    
    return user_info