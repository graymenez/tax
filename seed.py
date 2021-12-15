from models import db,User
from app import app



db.drop_all()
db.create_all()

first_name = ['Chris','Katy','John','Richard']
last_name = ['Kyle','Ferris','Wick','Dickerson']
admin_status = ['t']
email = ['ChrisK@example.com','KatyF@example.com','JohnW@example.com','RichardD@example.com']
password = ['Paramedic101','Firefighter101','Police101','EMT101']

new_users = [User.register(first_name=f,last_name=l,email=e,password=p) for f,l,e,p in zip(first_name,last_name,email,password)]

db.session.add_all(new_users)
db.session.commit()