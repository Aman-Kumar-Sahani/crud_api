from mongoengine import Document ,fields,connect
connect('mongotask')

class User(Document):
    email = fields.StringField(max_length=100)
    username = fields.StringField(max_length=50)
    password = fields.StringField(max_length = 100)

# user = User(email = 'aman@gmail.com') 
# user.username = 'userdead'
# user.password='aman@1999'
# user.save()