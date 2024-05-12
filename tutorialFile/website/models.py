from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

#put test
#fetch test
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    lost_item = db.relationship('Lostitem')
    found_item = db.relationship('Founditem')

class Lostitem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    perru = db.Column(db.String(1000))             #it will crash if perru is changed. try click refresh and reset cache in browser next time
    description = db.Column(db.String(999999))
    date_lost = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    image_file = db.Column(db.Text, nullable=False)
    image_name = db.Column(db.Text, nullable=False)
    image_mimetype = db.Column(db.Text, nullable=False)

class Founditem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.String(999999))
    date_found = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    image_file = db.Column(db.Text, nullable=False)
