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
from app.diagnosa.forms import (
    DiagnosaForm
)
from app.decorators import admin_required
from app.email import send_email
from app.models import EditableHTML, Role, User, Pasien, Label, Pilihan

diagnosa = Blueprint('diagnosa', __name__)


@diagnosa.route('/')
@login_required
@admin_required
def index():
    """Index Diagnosa page."""
    diagnosa = Pasien.query.all()
    pilihans = Pilihan.query.all()
    labels = Label.query.all()
    return render_template('training/index.html', diagnosa=diagnosa, pilihans=pilihans, labels=labels) 

@diagnosa.route('/new-data', methods=['GET', 'POST'])
@login_required
@admin_required
def new_data():
    """Create a new data training."""
    form = DiagnosaForm()
    if form.validate_on_submit():
        datatraining = Training(
            name=form.name.data,
            k1=form.k1.data,
            k2=form.k2.data,
            k3=form.k3.data,
            k4=form.k4.data,
            k5=form.k5.data,
            k6=form.k6.data,
            k7=form.k7.data,
            c=form.c.data)
        db.session.add(datatraining)
        db.session.commit()
        flash('Data training {} successfully created'.format(datatraining.name),
              'form-success')
    return render_template('training/new_data.html', form=form)

@diagnosa.route('/change/<id>', methods=['GET', 'POST'])
@login_required
@admin_required
def change(id):
    """Create a change data training."""
    datatraining = Pasien.query.filter_by(id=id).first()
    form = DiagnosaForm(obj=datatraining)
    if form.validate_on_submit():
        datatraining.name = form.name.data
        datatraining.k1=form.k1.data,
        datatraining.k2=form.k2.data,
        datatraining.k3=form.k3.data,
        datatraining.k4=form.k4.data,
        datatraining.k5=form.k5.data,
        datatraining.k6=form.k6.data,
        datatraining.k7=form.k7.data,
        datatraining.c=form.c.data
        db.session.add(datatraining)
        db.session.commit()
        flash('Data training {} successfully changed'.format(datatraining.name),
              'form-success')
    return render_template('training/change_data.html', form=form)

@diagnosa.route('/delete/<int:data_id>')
@login_required
@admin_required
def delete(data_id):
    """Delete a data training."""
    
    data = Training.query.filter_by(id=data_id).first()
    db.session.delete(data)
    db.session.commit()
    flash('Successfully deleted data %s.' % data.name, 'success')
    return redirect(url_for('training.index'))