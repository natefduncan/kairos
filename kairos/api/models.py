from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):    
    id = db.Column(db.Integer, primary_key=True)    
    first_name = db.Column(db.String(100))    
    last_name = db.Column(db.String(100))    
    
    def __init__(self, first_name, last_name):        
        self.first_name = first_name        
        self.last_name = last_name