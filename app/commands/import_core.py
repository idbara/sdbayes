import json
import os

from sqlalchemy import exc

from app import db
from app.models import Label, Pilihan, Role, Training, User


def import_pilihan():
    """Import Data Pilihan to Database"""
    file = os.path.abspath('app/resources') + "/pilihan.json"
    json_data = open(file).read()
    json_obj = json.loads(json_data)
    for row in json_obj:
        try:
            data = Pilihan(id=row['id'], item=row['item'])
            db.session.add(data)
            db.session.commit()
            print('Import data pilihan {} done.'.format(data.item))
        except exc.IntegrityError:
            print('Data pilihan {} already exists'.format(data.item))
            db.session.rollback()


def import_label():
    """Import Data Label to Database"""
    file = os.path.abspath('app/resources') + "/label.json"
    json_data = open(file).read()
    json_obj = json.loads(json_data)
    for row in json_obj:
        try:
            data = Label(id=row['id'], item=row['item'])
            db.session.add(data)
            db.session.commit()
            print('Import data label {} done.'.format(data.item))
        except exc.IntegrityError:
            print('Data label {} already exists'.format(data.item))
            db.session.rollback()


def import_roles():
    """Import Data Role to Database"""
    file = os.path.abspath('app/resources') + "/roles.json"
    json_data = open(file).read()
    json_obj = json.loads(json_data)
    for row in json_obj:
        try:
            data = Role(id=row['id'],
                        name=row['name'],
                        index=row['index'],
                        default=row['default'],
                        permissions=row['permissions'])
            db.session.add(data)
            db.session.commit()
            print('Import data role {} done.'.format(data.name))
        except exc.IntegrityError:
            print('Data role {} already exists'.format(data.name))
            db.session.rollback()


def import_datatraining():
    """Import Data Data Training to Database"""
    file = os.path.abspath('app/resources') + "/datatraining.json"
    json_data = open(file).read()
    json_obj = json.loads(json_data)
    for row in json_obj:
        try:
            data = Training(name=row['name'],
                            k1=row['k1'],
                            k2=row['k2'],
                            k3=row['k3'],
                            k4=row['k4'],
                            k5=row['k5'],
                            k6=row['k6'],
                            k7=row['k7'],
                            c=row['c'])
            db.session.add(data)
            db.session.commit()
            print('Import data data training {} done.'.format(data.name))
        except exc.IntegrityError:
            print('Data data training {} already exists'.format(data.name))
            db.session.rollback()
