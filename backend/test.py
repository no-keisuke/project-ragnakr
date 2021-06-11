import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

default_app = firebase_admin.initialize_app()
print(default_app.name)  # "[DEFAULT]"
# user = auth.create_user(
#     email='hello@example.com',
#     password='secretPassword',
#     display_name='John Doe',
# 	)
    
# print('Sucessfully created new user: {0}'.format(user.uid))
user = auth.get_user_by_email('hello@example.com')
print('Successfully fetched user data: {0}'.format(user.uid))
