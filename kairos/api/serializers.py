from marshmallow_sqlalchemy import SQLAlchemySchema
from models import *


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True
