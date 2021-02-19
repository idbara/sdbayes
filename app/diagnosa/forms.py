from flask_wtf import FlaskForm
from wtforms.fields import (
    SelectField,
    StringField,
    SubmitField,
)
from wtforms.validators import DataRequired, InputRequired, Length

from app.models import Label, Pilihan


class DiagnosaForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired(), Length(1, 64)])
    k1 = SelectField(
        "Merasa gelisah, cemas atau amat tegang :",
        validators=[DataRequired()],
        coerce=int,
    )
    k2 = SelectField(
        "Tidak mampu menghentikan atau mengendalikan rasa khawatir :",
        validators=[DataRequired()],
        coerce=int,
    )
    k3 = SelectField(
        "Terlalu mengkhawatirkan berbagai hal :",
        validators=[DataRequired()],
        coerce=int,
    )
    k4 = SelectField("Sulit untuk santai :", validators=[DataRequired()], coerce=int)
    k5 = SelectField(
        "Sangat gelisah sehingga sulit untuk duduk diam :",
        validators=[DataRequired()],
        coerce=int,
    )
    k6 = SelectField(
        "Menjadi mudah jengkel atau lekas marah :",
        validators=[DataRequired()],
        coerce=int,
    )
    k7 = SelectField(
        "Merasa takut seolah-olah sesuatu yang mengerikan/buruk mungkin terjadi :",
        validators=[DataRequired()],
        coerce=int,
    )
    c = SelectField("Tingkat kecemasam :", validators=[DataRequired()], coerce=int)
    submit = SubmitField("Save")

    def __init__(self, *args, **kwargs):
        super(DiagnosaForm, self).__init__(*args, **kwargs)
        self.k1.choices = [
            (row.id, row.item) for row in Pilihan.query.order_by("id").all()
        ]
        self.k2.choices = [
            (row.id, row.item) for row in Pilihan.query.order_by("id").all()
        ]
        self.k3.choices = [
            (row.id, row.item) for row in Pilihan.query.order_by("id").all()
        ]
        self.k4.choices = [
            (row.id, row.item) for row in Pilihan.query.order_by("id").all()
        ]
        self.k5.choices = [
            (row.id, row.item) for row in Pilihan.query.order_by("id").all()
        ]
        self.k6.choices = [
            (row.id, row.item) for row in Pilihan.query.order_by("id").all()
        ]
        self.k7.choices = [
            (row.id, row.item) for row in Pilihan.query.order_by("id").all()
        ]
        self.c.choices = [
            (row.id, row.item) for row in Label.query.order_by("id").all()
        ]


class PrintLaporan(FlaskForm):
    bulan_CHOICES = [('01-2021', 'Januari 2021'), ('02-2021', 'Februari 2021')]

    bulan = SelectField("Month", validators=[DataRequired()], choices=bulan_CHOICES)
    submit = SubmitField('Submit')

