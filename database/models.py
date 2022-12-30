from peewee import *
from data.config import DB_NAME, DB_USER, DB_HOST, DB_PASSWORD, DB_PORT

db = PostgresqlDatabase(DB_NAME, user=DB_USER, host=DB_HOST, password=DB_PASSWORD, port=DB_PORT)


class BaseModel(Model):
    class Meta:
        database = db

        
class Users(BaseModel):
    user_id = BigIntegerField(primary_key=True)
    username = CharField(max_length=200, null=True)

    class Meta:
        db_name = 'users'
