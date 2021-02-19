import datetime
from sqlalchemy.ext.hybrid import hybrid_property
from .. import db


class Diagnosa(db.Model):
    __tablename__ = "datadiagnosa"
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey("users.id"))
    tingkatkecemasan = db.Column(db.String(64))
    sedikitatautidakada = db.Column(db.Float)
    ringan = db.Column(db.Float)
    sedang = db.Column(db.Float)
    parah = db.Column(db.Float)
    datetime = db.Column(db.DateTime, default=datetime.datetime.utcnow)


    def __repr__(self):
        return "<Diagnosa {}>".format(self.user)
