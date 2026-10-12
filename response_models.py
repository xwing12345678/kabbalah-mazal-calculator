
from peewee import*
import os
db_url=os.getenv("DB_NAME")
db = SqliteDatabase(database=db_url, pragmas={'foreign_keys': 1})

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
        id = AutoField()
        username = CharField(null=False)
        email = CharField(null=False)
        password_hash = CharField(null=False)
        class Meta:
            db_table = 'users'

class Person(BaseModel):
    user_id = ForeignKeyField(User, backref='user_id')
    user_relationship = CharField(null=True)
    hebrew_personal_name = CharField(null=False)
    hebrew_mother_personal_name= CharField(null=False)
    birthdate = DateField(null=True)
    birth_time = TimeField(null=True)
    birth_night_flag = BooleanField(null=True)
    birth_location = CharField(null=True)

    class Meta:
        db_table = 'people_info'





