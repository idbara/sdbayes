from flask import url_for
from flask_wtf import FlaskForm
from wtforms import ValidationError
from wtforms.fields import (BooleanField, PasswordField, SelectField,
                            StringField, SubmitField)
from wtforms.fields.html5 import EmailField
from wtforms.validators import (DataRequired, Email, EqualTo, InputRequired,
                                Length)

from app.models import Label, Pasien, Pilihan, Role, User


class PasienForm(FlaskForm):
    user = SelectField('Pasien :', validators=[DataRequired()], coerce=int)
    k1 = SelectField('Merasa gelisah, cemas atau amat tegang :',
                     validators=[DataRequired()],
                     coerce=int)
    k2 = SelectField(
        'Tidak mampu menghentikan atau mengendalikan rasa khawatir :',
        validators=[DataRequired()],
        coerce=int)
    k3 = SelectField('Terlalu mengkhawatirkan berbagai hal :',
                     validators=[DataRequired()],
                     coerce=int)
    k4 = SelectField('Sulit untuk santai :',
                     validators=[DataRequired()],
                     coerce=int)
    k5 = SelectField('Sangat gelisah sehingga sulit untuk duduk diam :',
                     validators=[DataRequired()],
                     coerce=int)
    k6 = SelectField('Menjadi mudah jengkel atau lekas marah :',
                     validators=[DataRequired()],
                     coerce=int)
    k7 = SelectField(
        'Merasa takut seolah-olah sesuatu yang mengerikan/buruk mungkin terjadi :',
        validators=[DataRequired()],
        coerce=int)
    submit = SubmitField('Save')

    def __init__(self, *args, **kwargs):
        super(PasienForm, self).__init__(*args, **kwargs)
        # User.query.all()
        self.user.choices = [
            (row.id, row.full_name())
            # for row in User.query.all()
            for row in User.query.filter_by(role_id=1).all()
        ]
        self.k1.choices = [(row.id, row.item)
                           for row in Pilihan.query.order_by('id').all()]
        self.k2.choices = [(row.id, row.item)
                           for row in Pilihan.query.order_by('id').all()]
        self.k3.choices = [(row.id, row.item)
                           for row in Pilihan.query.order_by('id').all()]
        self.k4.choices = [(row.id, row.item)
                           for row in Pilihan.query.order_by('id').all()]
        self.k5.choices = [(row.id, row.item)
                           for row in Pilihan.query.order_by('id').all()]
        self.k6.choices = [(row.id, row.item)
                           for row in Pilihan.query.order_by('id').all()]
        self.k7.choices = [(row.id, row.item)
                           for row in Pilihan.query.order_by('id').all()]

    def validate_pasien(self, field):
        if Pasien.query.filter_by(user=field.data).first():
            raise ValidationError('User already. (Did you mean to '
                                  '<a href="{}">Check</a>?)'.format(
                                      url_for('pasien.index')))


class PasienInputForm(FlaskForm):
    # user = StringField('Nama', validators=[InputRequired(),
    #                               Length(1, 64)])
    k1 = SelectField('Merasa gelisah, cemas atau amat tegang :',
                     validators=[DataRequired()],
                     coerce=int)
    k2 = SelectField(
        'Tidak mampu menghentikan atau mengendalikan rasa khawatir :',
        validators=[DataRequired()],
        coerce=int)
    k3 = SelectField('Terlalu mengkhawatirkan berbagai hal :',
                     validators=[DataRequired()],
                     coerce=int)
    k4 = SelectField('Sulit untuk santai :',
                     validators=[DataRequired()],
                     coerce=int)
    k5 = SelectField('Sangat gelisah sehingga sulit untuk duduk diam :',
                     validators=[DataRequired()],
                     coerce=int)
    k6 = SelectField('Menjadi mudah jengkel atau lekas marah :',
                     validators=[DataRequired()],
                     coerce=int)
    k7 = SelectField(
        'Merasa takut seolah-olah sesuatu yang mengerikan/buruk mungkin terjadi :',
        validators=[DataRequired()],
        coerce=int)
    submit = SubmitField('Save')

    def __init__(self, *args, **kwargs):
        super(PasienInputForm, self).__init__(*args, **kwargs)

        self.k1.choices = [(row.id, row.item)
                           for row in Pilihan.query.order_by('id').all()]
        self.k2.choices = [(row.id, row.item)
                           for row in Pilihan.query.order_by('id').all()]
        self.k3.choices = [(row.id, row.item)
                           for row in Pilihan.query.order_by('id').all()]
        self.k4.choices = [(row.id, row.item)
                           for row in Pilihan.query.order_by('id').all()]
        self.k5.choices = [(row.id, row.item)
                           for row in Pilihan.query.order_by('id').all()]
        self.k6.choices = [(row.id, row.item)
                           for row in Pilihan.query.order_by('id').all()]
        self.k7.choices = [(row.id, row.item)
                           for row in Pilihan.query.order_by('id').all()]

    def validate_pasien(self, field):
        if Pasien.query.filter_by(user=field.data).first():
            raise ValidationError('User already. (Did you mean to '
                                  '<a href="{}">Check</a>?)'.format(
                                      url_for('pasien.index')))
