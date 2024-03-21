from athours_app import db
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Company(db.Model):
    
    __tablename__="companies"
    id=db.Column(db.Integer,primary_key=True)#all datatypes start with capital letter eg Integer,String
    name=db.Column(db.String(50),nullable=False)
    origin=db.Column(db.String(100))
    description=db.Column(db.String(1000),nullable=False,unique=True)
    #user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    #user=db.relationship("users",backref="companies")
    created_at=db.Column(db.DateTime,default=datetime.now())
    updated_at=db.Column(db.DateTime,onupdate=datetime.now())

def __init__(self,name,description,origin):
    self.name=name
    self.description=description
    self.origin=origin


    def __init__(self):
        return f"<company(name='{self.name}',origin='{self.origin}')"