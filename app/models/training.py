from .. import db


class Pilihan(db.Model):
    __tablename__ = 'pilihan'
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Pilihan {}>'.format(self.item)


class Label(db.Model):
    __tablename__ = 'label'
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Label {}>'.format(self.item)


class Training(db.Model):
    __tablename__ = 'datatraining'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    k1 = db.Column(db.Integer, db.ForeignKey('pilihan.id'))
    k2 = db.Column(db.Integer, db.ForeignKey('pilihan.id'))
    k3 = db.Column(db.Integer, db.ForeignKey('pilihan.id'))
    k4 = db.Column(db.Integer, db.ForeignKey('pilihan.id'))
    k5 = db.Column(db.Integer, db.ForeignKey('pilihan.id'))
    k6 = db.Column(db.Integer, db.ForeignKey('pilihan.id'))
    k7 = db.Column(db.Integer, db.ForeignKey('pilihan.id'))
    c = db.Column(db.Integer, db.ForeignKey('label.id'))

    def __repr__(self):
        return '<Training {}>'.format(self.name)
