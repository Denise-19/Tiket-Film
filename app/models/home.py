from datetime import datetime
from app import db, ma


class string(db.Model):
    __tablename__ = "string"
    id = db.Column(db.Integer, primary_key=True)
    input = db.Column(db.String(255))
    last_modified = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<Kelas a {}>'.format(self.input)


class stringSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = string
        load_instance = True


class integer(db.Model):
    __tablename__ = "integer"
    id = db.Column(db.Integer, primary_key=True)
    input = db.Column(db.Integer)
    last_modified = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<Kelas B {}>'.format(self.input)


class integerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = integer
        load_instance = True
