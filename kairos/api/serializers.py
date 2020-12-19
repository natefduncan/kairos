from models import *
from marshmallow_sqlalchemy import SQLAlchemySchema

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True