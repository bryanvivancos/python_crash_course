favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python'
}

poll = ['jen','sarah','oscar','edward','phil','bryan','karl']

for poller in poll: 
    if poller in favorite_languages.keys():
        print(f"\n {poller.title()}, thanks you for responding")
    else:
        print(f"\n {poller.title()}, we invite you to take the poll")