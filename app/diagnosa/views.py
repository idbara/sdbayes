from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
    jsonify
)
from flask_login import current_user, login_required
from flask_rq import get_queue

from app import db
from app.diagnosa.forms import (
    DiagnosaForm
)
from app.decorators import admin_required
from app.email import send_email
from app.models import EditableHTML, Role, User, Pasien, Label, Pilihan,Diagnosa, Training

from app.diagnosa.bayes import getDataTraining,getJumlahData,getJumlahKriteria,getJumlahC,bayes
import json


diagnosa = Blueprint('diagnosa', __name__)

@diagnosa.route('/datatraining')
@login_required
@admin_required
def getData():
    d = bayes(2)
    return str(d[2][0][1])
    # data = Pasien.query.filter_by(id=1).first()
    # return str(data.k1)

@diagnosa.route('/')
@login_required
@admin_required
def index():
    """Index Diagnosa page."""
    diagnosa = Pasien.query.join(User, Pasien.user == User.id).join(Diagnosa, Pasien.user == Diagnosa.user).add_columns(Pasien.id,User.first_name.label('first_name'),User.last_name.label('last_name'),Pasien.k1,Pasien.k2,Pasien.k3,Pasien.k4,Pasien.k5,Pasien.k6,Pasien.k7,Diagnosa.tingkatkecemasan,Diagnosa.sedikitatautidakada,Diagnosa.ringan,Diagnosa.sedang,Diagnosa.parah).all()
    pilihans = Pilihan.query.all()
    labels = Label.query.all()
    return render_template('diagnosa/index.html', diagnosa=diagnosa, pilihans=pilihans, labels=labels) 

@diagnosa.route('/detail/<id>', methods=['GET', 'POST'])
@login_required
@admin_required
def detail(id):
    """Create a change data training."""
    trainings = Training.query.all()
    pilihans = Pilihan.query.all()
    labels = Label.query.all()
    
    return render_template('diagnosa/detail.html', trainings=trainings, pilihans=pilihans, labels=labels)