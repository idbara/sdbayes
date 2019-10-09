from flask import url_for
from flask_wtf import FlaskForm
from wtforms import ValidationError
from wtforms.fields import (
    BooleanField,
    PasswordField,
    StringField,
    SubmitField,
    SelectField,
)
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, EqualTo, InputRequired, Length, DataRequired

from app.models import User,Pilihan,Label

class TestingForm(FlaskForm):
    name = StringField(
        'Name', validators=[InputRequired(),
                                  Length(1, 64)])
    k1 = SelectField('Merasa gelisah, cemas atau amat tegang :',
                           validators=[DataRequired()],
                           coerce=int)
    k2 = SelectField('Tidak mampu menghentikan atau mengendalikan rasa khawatir :',
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
    k7 = SelectField('Merasa takut seolah-olah sesuatu yang mengerikan/buruk mungkin terjadi :',
                           validators=[DataRequired()],
                           coerce=int)
    c = SelectField('Tingkat kecemasam :',
                           validators=[DataRequired()],
                           coerce=int)
    submit = SubmitField('Save')

    def __init__(self, *args, **kwargs):
        super(TestingForm, self).__init__(*args, **kwargs)
        self.k1.choices = [
            (row.id, row.item)
            for row in Pilihan.query.order_by('id').all()
        ]
        self.k2.choices = [
            (row.id, row.item)
            for row in Pilihan.query.order_by('id').all()
        ]
        self.k3.choices = [
            (row.id, row.item)
            for row in Pilihan.query.order_by('id').all()
        ]
        self.k4.choices = [
            (row.id, row.item)
            for row in Pilihan.query.order_by('id').all()
        ]
        self.k5.choices = [
            (row.id, row.item)
            for row in Pilihan.query.order_by('id').all()
        ]
        self.k6.choices = [
            (row.id, row.item)
            for row in Pilihan.query.order_by('id').all()
        ]
        self.k7.choices = [
            (row.id, row.item)
            for row in Pilihan.query.order_by('id').all()
        ]
        self.c.choices = [
            (row.id, row.item)
            for row in Label.query.order_by('id').all()
        ]