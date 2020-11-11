from _operator import itemgetter

import pandas as pd

from flask import (Blueprint, abort, flash, jsonify, redirect, render_template,
                   request, url_for)
from flask_login import current_user, login_required
from flask_rq import get_queue

from app import db
from app.decorators import admin_required, pasien_required
from app.diagnosa.bayes import (bayes, getAtribut, getC,
                                getJumlahC, getJumlahKriteria,
                                likehood)
from app.diagnosa.forms import DiagnosaForm
from app.email import send_email
from app.models import Diagnosa, Label, Pasien, Pilihan, Role, Training, User

diagnosa = Blueprint('diagnosa', __name__)


@diagnosa.route('/test/<id>', methods=['GET', 'POST'])
@login_required
@admin_required
def test(id):
    pasien = Pasien.query.filter_by(id=id).first()
    datatraining = pd.read_sql_table('datatraining', db.session.bind)
    def getJumlahKriteria(kriteria, y, z):
        jmlkriteria = datatraining[(datatraining[kriteria] == y) & (datatraining['c'] == z)]
        return len(jmlkriteria.index)

    def getJumlahC(z):
        jmlC = datatraining[datatraining['c'] == z]
        return len(jmlC.index)

    def bayes(pasien):
        # P(Ci)
        SumPCi = getJumlahC(1) + getJumlahC(2) + getJumlahC(3) + getJumlahC(4)
        PCisedikit = getJumlahC(1) / SumPCi
        PCiringan = getJumlahC(2) / SumPCi
        PCisedang = getJumlahC(3) / SumPCi
        PCiparah = getJumlahC(4) / SumPCi

        # P(Merasa gelisah, cemas atau amat tegang|Ci)
        P1C1 = getJumlahKriteria('k1', pasien.k1, 1) / getJumlahC(1)
        P1C2 = getJumlahKriteria('k1', pasien.k1, 2) / getJumlahC(2)
        P1C3 = getJumlahKriteria('k1', pasien.k1, 3) / getJumlahC(3)
        P1C4 = getJumlahKriteria('k1', pasien.k1, 4) / getJumlahC(4)

        # P(Tidak mampu menghentikan atau mengendalikan rasa khawatir|Ci)
        P2C1 = getJumlahKriteria('k2', pasien.k2, 1) / getJumlahC(1)
        P2C2 = getJumlahKriteria('k2', pasien.k2, 2) / getJumlahC(2)
        P2C3 = getJumlahKriteria('k2', pasien.k2, 3) / getJumlahC(3)
        P2C4 = getJumlahKriteria('k2', pasien.k2, 4) / getJumlahC(4)

        # P(Terlalu mengkhawatirkan berbagai hal|Ci)
        P3C1 = getJumlahKriteria('k3', pasien.k3, 1) / getJumlahC(1)
        P3C2 = getJumlahKriteria('k3', pasien.k3, 2) / getJumlahC(2)
        P3C3 = getJumlahKriteria('k3', pasien.k3, 3) / getJumlahC(3)
        P3C4 = getJumlahKriteria('k3', pasien.k3, 4) / getJumlahC(4)

        # P(Sulit untuk santai |Ci)
        P4C1 = getJumlahKriteria('k4', pasien.k4, 1) / getJumlahC(1)
        P4C2 = getJumlahKriteria('k4', pasien.k4, 2) / getJumlahC(2)
        P4C3 = getJumlahKriteria('k4', pasien.k4, 3) / getJumlahC(3)
        P4C4 = getJumlahKriteria('k4', pasien.k4, 4) / getJumlahC(4)

        # P(Sangat gelisah sehingga sulit untuk duduk diam |Ci)
        P5C1 = getJumlahKriteria('k5', pasien.k5, 1) / getJumlahC(1)
        P5C2 = getJumlahKriteria('k5', pasien.k5, 2) / getJumlahC(2)
        P5C3 = getJumlahKriteria('k5', pasien.k5, 3) / getJumlahC(3)
        P5C4 = getJumlahKriteria('k5', pasien.k5, 4) / getJumlahC(4)

        # P(Menjadi mudah jengkel atau lekas marah |Ci)
        P6C1 = getJumlahKriteria('k6', pasien.k6, 1) / getJumlahC(1)
        P6C2 = getJumlahKriteria('k6', pasien.k6, 2) / getJumlahC(2)
        P6C3 = getJumlahKriteria('k6', pasien.k6, 3) / getJumlahC(3)
        P6C4 = getJumlahKriteria('k6', pasien.k6, 4) / getJumlahC(4)

        # P(Merasa takut seolah-olah sesuatu yang mengerikan/buruk mungkin terjadi |Ci)
        P7C1 = getJumlahKriteria('k7', pasien.k7, 1) / getJumlahC(1)
        P7C2 = getJumlahKriteria('k7', pasien.k7, 2) / getJumlahC(2)
        P7C3 = getJumlahKriteria('k7', pasien.k7, 3) / getJumlahC(3)
        P7C4 = getJumlahKriteria('k7', pasien.k7, 4) / getJumlahC(4)

        # P(X|Ci)*P(Ci)
        C1 = PCisedikit * (P1C1 * P2C1 * P3C1 * P4C1 * P5C1 * P6C1 * P7C1)
        C2 = PCiringan * (P1C2 * P2C2 * P3C2 * P4C2 * P5C2 * P6C2 * P7C2)
        C3 = PCisedang * (P1C3 * P2C3 * P3C3 * P4C3 * P5C3 * P6C3 * P7C3)
        C4 = PCiparah * (P1C4 * P2C4 * P3C4 * P4C4 * P5C4 * P6C4 * P7C4)

        # Probabilitas akhir
        SumC = C1 + C2 + C3 + C4
        PC1 = C1 / SumC
        PC2 = C2 / SumC
        PC3 = C3 / SumC
        PC4 = C4 / SumC

        result = (("Sedikit atau tidak ada", PC1), ("Ringan", PC2), ("Sedang", PC3),
                  ("Parah", PC4))

        sortResult = sorted(result, key=itemgetter(1), reverse=True)
        print(sortResult)

        # tingkat kecemasan
        tk = sortResult[0][0]
        result = (pasien.user, tk, (sortResult))
        return result

    return str(bayes(pasien))


@diagnosa.route('/')
@login_required
@admin_required
def index():
    """Index Diagnosa page."""
    diagnosa = Pasien.query.join(User, Pasien.user == User.id).join(
        Diagnosa, Pasien.user == Diagnosa.user).add_columns(
            Pasien.id, User.first_name.label('first_name'),
            User.last_name.label('last_name'), Pasien.k1, Pasien.k2, Pasien.k3,
            Pasien.k4, Pasien.k5, Pasien.k6, Pasien.k7,
            Diagnosa.tingkatkecemasan, Diagnosa.sedikitatautidakada,
            Diagnosa.ringan, Diagnosa.sedang, Diagnosa.parah).all()
    pilihans = Pilihan.query.all()
    labels = Label.query.all()
    return render_template('diagnosa/index.html',
                           diagnosa=diagnosa,
                           pilihans=pilihans,
                           labels=labels)


@diagnosa.route('/detail/<id>', methods=['GET', 'POST'])
@login_required
@admin_required
def detail(id):
    """Detail data diagnosa."""
    trainings = Training.query.all()
    pilihans = Pilihan.query.all()
    labels = Label.query.all()
    diagnosa = Pasien.query.filter_by(id=id).join(
        User, Pasien.user == User.id).add_columns(
            Pasien.id, User.first_name.label('first_name'),
            User.last_name.label('last_name'), Pasien.k1, Pasien.k2, Pasien.k3,
            Pasien.k4, Pasien.k5, Pasien.k6, Pasien.k7, Pasien.user).first()
    k1 = getAtribut('k1')
    k2 = getAtribut('k2')
    k3 = getAtribut('k3')
    k4 = getAtribut('k4')
    k5 = getAtribut('k5')
    k6 = getAtribut('k6')
    k7 = getAtribut('k7')
    c = getC()
    lh = likehood(id)
    hasildiagnosa = Diagnosa.query.filter_by(user=diagnosa.user).add_columns(
        Diagnosa.tingkatkecemasan).first()
    return render_template('diagnosa/detail.html',
                           trainings=trainings,
                           pilihans=pilihans,
                           labels=labels,
                           diagnosa=diagnosa,
                           k1=k1,
                           k2=k2,
                           k3=k3,
                           k4=k4,
                           k5=k5,
                           k6=k6,
                           k7=k7,
                           c=c,
                           lh=lh,
                           hasildiagnosa=hasildiagnosa)


@diagnosa.route('/pasien/<id>', methods=['GET', 'POST'])
@login_required
@pasien_required
def pasien(id):
    if Pasien.query.filter_by(user=id).count() != 0:
        """data diagnosa."""
        trainings = Training.query.all()
        pilihans = Pilihan.query.all()
        labels = Label.query.all()
        diagnosa = Pasien.query.filter_by(user=id).join(
            User, Pasien.user == User.id).add_columns(
                Pasien.id, User.first_name.label('first_name'),
                User.last_name.label('last_name'), Pasien.k1, Pasien.k2,
                Pasien.k3, Pasien.k4, Pasien.k5, Pasien.k6, Pasien.k7,
                Pasien.user).first()
        k1 = getAtribut('k1')
        k2 = getAtribut('k2')
        k3 = getAtribut('k3')
        k4 = getAtribut('k4')
        k5 = getAtribut('k5')
        k6 = getAtribut('k6')
        k7 = getAtribut('k7')
        c = getC()
        lh = likehood(diagnosa.id)
        hasildiagnosa = Diagnosa.query.filter_by(user=diagnosa.user).first()
        return render_template('diagnosa/pasien.html',
                               trainings=trainings,
                               pilihans=pilihans,
                               labels=labels,
                               diagnosa=diagnosa,
                               k1=k1,
                               k2=k2,
                               k3=k3,
                               k4=k4,
                               k5=k5,
                               k6=k6,
                               k7=k7,
                               c=c,
                               lh=lh,
                               hasildiagnosa=hasildiagnosa)
    else:
        flash('Data pasien {} harus diisi'.format(current_user.full_name()),
              'warning')
        return redirect(url_for('pasien.input'))


@diagnosa.route('/pasien/detail/<id>', methods=['GET', 'POST'])
@login_required
@pasien_required
def pasien_detail(id):
    """Detail data diagnosa."""
    trainings = Training.query.all()
    pilihans = Pilihan.query.all()
    labels = Label.query.all()
    diagnosa = Pasien.query.filter_by(user=id).join(
        User, Pasien.user == User.id).add_columns(
            Pasien.id, User.first_name.label('first_name'),
            User.last_name.label('last_name'), Pasien.k1, Pasien.k2, Pasien.k3,
            Pasien.k4, Pasien.k5, Pasien.k6, Pasien.k7, Pasien.user).first()
    k1 = getAtribut('k1')
    k2 = getAtribut('k2')
    k3 = getAtribut('k3')
    k4 = getAtribut('k4')
    k5 = getAtribut('k5')
    k6 = getAtribut('k6')
    k7 = getAtribut('k7')
    c = getC()
    lh = likehood(diagnosa.id)
    hasildiagnosa = Diagnosa.query.filter_by(user=diagnosa.user).add_columns(
        Diagnosa.tingkatkecemasan).first()
    return render_template('diagnosa/pasien_detail.html',
                           trainings=trainings,
                           pilihans=pilihans,
                           labels=labels,
                           diagnosa=diagnosa,
                           k1=k1,
                           k2=k2,
                           k3=k3,
                           k4=k4,
                           k5=k5,
                           k6=k6,
                           k7=k7,
                           c=c,
                           lh=lh,
                           hasildiagnosa=hasildiagnosa)
