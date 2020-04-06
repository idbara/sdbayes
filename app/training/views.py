from flask import (Blueprint, abort, flash, redirect, render_template, request,
                   url_for)
from flask_login import current_user, login_required
from flask_rq import get_queue

from app import db
from app.decorators import admin_required
from app.email import send_email
from app.models import Label, Pilihan, Role, Training, User
from app.training.forms import TrainingForm

training = Blueprint('training', __name__)


@training.route('/')
@login_required
@admin_required
def index():
    """Index Training page."""
    trainings = Training.query.all()
    pilihans = Pilihan.query.all()
    labels = Label.query.all()
    return render_template('training/index.html',
                           trainings=trainings,
                           pilihans=pilihans,
                           labels=labels)


@training.route('/new-data', methods=['GET', 'POST'])
@login_required
@admin_required
def new_data():
    """Create a new data training."""
    form = TrainingForm()
    if form.validate_on_submit():
        datatraining = Training(name=form.name.data,
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
        flash(
            'Data training {} successfully created'.format(datatraining.name),
            'form-success')
    return render_template('training/new_data.html', form=form)


@training.route('/change/<id>', methods=['GET', 'POST'])
@login_required
@admin_required
def change(id):
    """Create a change data training."""
    datatraining = Training.query.filter_by(id=id).first()
    form = TrainingForm(obj=datatraining)
    if form.validate_on_submit():
        datatraining.name = form.name.data
        datatraining.k1 = form.k1.data,
        datatraining.k2 = form.k2.data,
        datatraining.k3 = form.k3.data,
        datatraining.k4 = form.k4.data,
        datatraining.k5 = form.k5.data,
        datatraining.k6 = form.k6.data,
        datatraining.k7 = form.k7.data,
        datatraining.c = form.c.data
        db.session.add(datatraining)
        db.session.commit()
        flash(
            'Data training {} successfully changed'.format(datatraining.name),
            'form-success')
    return render_template('training/change_data.html', form=form)


@training.route('/delete/<int:data_id>')
@login_required
@admin_required
def delete(data_id):
    """Delete a data training."""

    data = Training.query.filter_by(id=data_id).first()
    db.session.delete(data)
    db.session.commit()
    flash('Successfully deleted data %s.' % data.name, 'success')
    return redirect(url_for('training.index'))
