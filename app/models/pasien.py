from flask import current_app
from flask_login import AnonymousUserMixin, UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from werkzeug.security import check_password_hash, generate_password_hash

from .. import db, login_manager

class Pasien(db.Model):
    __tablename__ = 'datapasien'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    k1 = db.Column(db.Integer, db.ForeignKey('pilihan.id'))
    k2 = db.Column(db.Integer, db.ForeignKey('pilihan.id'))
    k3 = db.Column(db.Integer, db.ForeignKey('pilihan.id'))
    k4 = db.Column(db.Integer, db.ForeignKey('pilihan.id'))
    k5 = db.Column(db.Integer, db.ForeignKey('pilihan.id'))
    k6 = db.Column(db.Integer, db.ForeignKey('pilihan.id'))
    k7 = db.Column(db.Integer, db.ForeignKey('pilihan.id'))

    def __repr__(self):
        return '<Pasien {}>'.format(self.user)