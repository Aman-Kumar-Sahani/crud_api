from mongoengine import Document ,fields,connect
connect('mongotask')


class Student(Document):
    first_name = fields.StringField(max_length=50)
    last_name = fields.StringField(max_length=50)
    email = fields.EmailField(required=True,unique=True)
    college = fields.StringField(max_length=150)
