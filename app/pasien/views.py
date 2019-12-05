from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import current_user, login_required
from flask_rq import get_queue

from app import db
from app.pasien.forms import (
    PasienForm
)
from app.decorators import admin_required
from app.email import send_email
from app.models import EditableHTML, Role, User, Pasien, Label, Pilihan,Diagnosa

from app.diagnosa.bayes import bayes

pasien = Blueprint('pasien', __name__)


@pasien.route('/')
@login_required
@admin_required
def index():
    """Index Pasien page."""
    pasien = Pasien.query.join(User, Pasien.user == User.id).add_columns(Pasien.id,User.first_name.label('first_name'),User.last_name.label('last_name'),Pasien.k1,Pasien.k2,Pasien.k3,Pasien.k4,Pasien.k5,Pasien.k6,Pasien.k7).all()
    pilihans = Pilihan.query.all()
    labels = Label.query.all()
    return render_template('pasien/index.html', pasien=pasien, pilihans=pilihans, labels=labels) 

@pasien.route('/new-data', methods=['GET', 'POST'])
@login_required
@admin_required
def new_data():
    """Create a new data pasien."""
    form = PasienForm()
    if form.validate_on_submit():
        if Pasien.query.filter_by(user=form.user.data).first():
            flash('Pasien already exists.','form-error')
        else:
            datapasien = Pasien(
                user=form.user.data,
                k1=form.k1.data,
                k2=form.k2.data,
                k3=form.k3.data,
                k4=form.k4.data,
                k5=form.k5.data,
                k6=form.k6.data,
                k7=form.k7.data)
            db.session.add(datapasien)
            db.session.commit()
            result = bayes(datapasien.id)
            data = Diagnosa(
                user=result[0],
                tingkatkecemasan = result[1],
                sedikitatautidakada = result[2][0][1],
                ringan = result[2][1][1],
                sedang = result[2][2][1],
                parah = result[2][3][1])
            db.session.add(data)
            db.session.commit()

            name = User.query.filter_by(id=form.user.data).first()
            flash('Data pasien {} successfully created & diagnosa'.format(name.full_name()),
                'form-success')
            # flash('Data pasien {} successfully created & diagnosa'.format(datapasien.id),
            #     'form-success')
    return render_template('pasien/new_data.html', form=form)

@pasien.route('/change/<id>', methods=['GET', 'POST'])
@login_required
@admin_required
def change(id):
    """Create a change data pasien."""
    # pasien = Pasien.query.join(User, Pasien.user == User.id).add_columns(Pasien.id,User.first_name.label('first_name'),User.last_name.label('last_name'),Pasien.k1,Pasien.k2,Pasien.k3,Pasien.k4,Pasien.k5,Pasien.k6,Pasien.k7).all()
    datapasien = Pasien.query.filter_by(id=id).first()
    form = PasienForm(obj=datapasien)
    if form.validate_on_submit():
        datapasien.user = form.user.data
        datapasien.k1=form.k1.data,
        datapasien.k2=form.k2.data,
        datapasien.k3=form.k3.data,
        datapasien.k4=form.k4.data,
        datapasien.k5=form.k5.data,
        datapasien.k6=form.k6.data,
        datapasien.k7=form.k7.data
        db.session.add(datapasien)
        db.session.commit()
        result = bayes(datapasien.id)
        data = Diagnosa.query.filter_by(user=datapasien.user).first()
        data.user=result[0]
        data.tingkatkecemasan = result[1]
        data.sedikitatautidakada = result[2][0][1]
        data.ringan = result[2][1][1]
        data.sedang = result[2][2][1]
        data.parah = result[2][3][1]
        db.session.add(data)
        db.session.commit()
        name = User.query.filter_by(id=form.user.data).first()
        flash('Data pasien {} successfully changed'.format(name.full_name()),
              'form-success')
    return render_template('pasien/change_data.html', form=form)

@pasien.route('/delete/<int:data_id>')
@login_required
@admin_required
def delete(data_id):
    """Delete a data pasien."""
    data = Pasien.query.filter_by(id=data_id).first()
    user = User.query.filter_by(id=data.user).first()
    db.session.delete(data)
    db.session.commit()
    flash('Successfully deleted data %s.' % user.full_name(), 'success')
    return redirect(url_for('pasien.index'))