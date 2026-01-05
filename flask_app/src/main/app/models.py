from flask_login import UserMixin
from . import db

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True) 
    password = db.Column(db.String(100), nullable=False) 
    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'))
    bookings = db.relationship('Booking', backref='user')

    def get_id(self):
        return str(self.user_id)

    def to_json(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password,
            'role_id': self.role_id

        }

class Role(db.Model):
    __tablename__ = 'roles'
    role_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def to_json(self):
        return {
            'role_id': self.role_id,
            'name': self.name
        }
    
class Park(db.Model):
    __tablename__ = 'parks'
    park_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    bookings = db.relationship('Booking', backref='park')

    def to_json(self):
        return {
            'park_id': self.park_id,
            'name': self.name,
            'location': self.location,
            'description': self.description 
        }

class Booking(db.Model):
    __tablename__ = 'bookings'
    booking_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    park_id = db.Column(db.Integer, db.ForeignKey('parks.park_id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    num_tickets = db.Column(db.Integer, nullable=False, default=1)
    health_safety = db.Column(db.Boolean, nullable=False, default=False)

    def to_json(self):
        return {
            'booking_id': self.booking_id,
            'user_id': self.user_id,
            'park_id': self.park_id,
            'date': self.date.isoformat(),
            'num_tickets': self.num_tickets,
            'health_safety':self.health_safety
        }