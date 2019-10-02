from app import db
import json
import os
from app.models import (Pilihan,Label,Role,User)
from sqlalchemy import exc


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
            data = Role(id=row['id'], name=row['name'],index=row['index'],default=row['default'],permissions=row['permissions'])
            db.session.add(data)
            db.session.commit()
            print('Import data role {} done.'.format(data.name))
        except exc.IntegrityError:
            print('Data role {} already exists'.format(data.name))
            db.session.rollback()

