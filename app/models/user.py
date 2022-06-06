from datetime import datetime
from app import db, ma
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = "user"

    id_user = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.VARCHAR(50), nullable=False)
    email = db.Column(db.VARCHAR(50))
    password = db.Column(db.String(128), nullable=False)
    last_modified = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def setPassword(self, password):
        self.password = generate_password_hash(password)
        return self.password

    def checkPassword(self, password):
        return check_password_hash(self.password, password)


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
