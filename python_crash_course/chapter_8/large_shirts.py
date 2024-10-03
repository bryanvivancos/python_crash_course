def make_shirt(text,size='Large',):
    print(f"\n'{size}' size Sshirt with the text '{text}'")

make_shirt('I love Python')

def make_shirt(size,text='I love JavaScript'):
    print(f"\n'{size}' size Shirt with the text '{text}'")
    
make_shirt('Large')
make_shirt('Medium')

def make_shirt(size='Small',text='I Love You'):
    print(f"\n'{size}' size Shirt with the text '{text}'")

make_shirt()