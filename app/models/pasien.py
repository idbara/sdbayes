from sqlalchemy.ext.hybrid import hybrid_property
from .. import db


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

    akun = db.relationship("User", backref="akun")

    @hybrid_property
    def name(self):
        return self.akun.full_name()

    def __repr__(self):
        return '<Pasien {}>'.format(self.user)
