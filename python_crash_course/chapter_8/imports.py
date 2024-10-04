import imports_functions
from imports_functions import make_shirt
from imports_functions import buildProfile as bp
import imports_functions as ifn
from imports_functions import *

# #testing first import
imports_functions.make_shirt('Medium','Work Hard') 

# #testing second import
make_shirt('Large','No escuses!')

# #testing third import
user_data = bp('Bryan','Vivanco',age=26,active=True)
print(user_data)

# #testing fourth import
user_profile = ifn.buildProfile('Sebástian','Vivanco',age = 19, rol='Student')
print(user_profile)

#testing fifth import
current_user = buildProfile('Ximena', 'Vivanco', age=17,email='ximenavivanco@gmail.com')
print(current_user)