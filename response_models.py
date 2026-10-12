
from peewee import*
import os
db_url=os.getenv("DB_NAME")
db = SqliteDatabase(db_url, pragmas={'foreign_keys': 1})

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
        id = AutoField()
        username = CharField
        email = CharField

        class Meta:
            db_table = 'users'

class Person(BaseModel):
    user_id = ForeignKeyField(User, backref='user_id')
    user_relationship = CharField
    hebrew_personal_name = CharField
    hebrew_mother_personal_name= CharField
    birthdate = DateField
    birth_time = TimeField
    birth_location = CharField

    class Meta:
        db_table = 'person_info'





