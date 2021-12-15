from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bcrypt=Bcrypt()

def connect_db(app):
    db.app=app
    db.init_app(app)


class User(db.Model):
    """User Model"""

    __tablename__='users'

    def __repr__(self):
        return f"{self.id},{self.first_name},{self.admin_status}"

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    first_name = db.Column(db.Text,nullable=False)
    last_name = db.Column(db.Text,nullable=False)
    admin_status = db.Column(db.Boolean,nullable=False,default=False)
    employee_status = db.Column(db.Boolean,nullable=False,default=False)
    email = db.Column(db.Text,nullable=False)
    password = db.Column(db.Text,nullable=False)
    phone = db.Column(db.Text,nullable=True)

    @classmethod
    def register(cls,first_name,last_name,email,password):
        hashed = bcrypt.generate_password_hash(password)

        hashed_pwd = hashed.decode('utf8')

        return cls(first_name=first_name,last_name=last_name,email=email,password=hashed_pwd)

    @classmethod
    def auth(cls,email,password):
        user = cls.query.filter_by(email = email).first()
        if user and bcrypt.check_password_hash(user.password,password):
            return user
        else:
            return False