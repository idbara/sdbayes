#!/usr/bin/env python
import os
import time
import subprocess

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
from flask_assets import ManageAssets
from redis import Redis
from rq import Connection, Queue, Worker

from app import create_app, db
from app.models import Role, User
from app.commands.import_core import (import_pilihan, import_label,
                                      import_roles, import_datatraining)
from config import Config

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
manager.add_command("assets", ManageAssets())
"""Run Import Core Data Using Commands"""


@manager.command
def import_dev():
    print("Preparing import core data")
    print("Please wait .....")
    time.sleep(2)
    import_core_data()
    print("Import core data has done")

    print("Preparing import training data")
    print("Please wait .....")
    time.sleep(2)
    import_data_training()
    print("Import training data has done")

    print("Preparing setup")
    print("Please wait .....")
    time.sleep(2)
    setup_general()
    print("setup has done")


"""Run Import Core Data Using Commands"""


@manager.command
def import_core_data():
    print("Preparing import pilihan data")
    print("Please wait .....")
    time.sleep(2)
    import_pilihan()
    print("Import pilihan data has done")

    print("Preparing import label data")
    print("Please wait .....")
    time.sleep(2)
    import_label()
    print("Import label data has done")

    print("Preparing import roles data")
    print("Please wait .....")
    time.sleep(2)
    import_roles()
    print("Import roles data has done")


"""Run Import Data Training Using Commands"""


@manager.command
def import_data_training():
    print("Preparing import data training data")
    print("Please wait .....")
    time.sleep(2)
    import_datatraining()
    print("Import data training has done")


@manager.command
def test():
    """Run the unit tests."""
    import unittest

    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def recreate_db():
    """
    Recreates a local database. You probably should not use this on
    production.
    """
    db.drop_all()
    db.create_all()
    db.session.commit()


@manager.option('-n',
                '--number-users',
                default=10,
                type=int,
                help='Number of each model type to create',
                dest='number_users')
def add_fake_data(number_users):
    """
    Adds fake data to the database.
    """
    User.generate_fake(count=number_users)


@manager.command
def setup_dev():
    """Runs the set-up needed for local development."""
    setup_general()


@manager.command
def setup_prod():
    """Runs the set-up needed for production."""
    setup_general()


def setup_general():
    """Runs the set-up needed for both local development and production.
       Also sets up first admin user."""
    # Role.insert_roles()
    admin_query = Role.query.filter_by(name='Administrator')
    if admin_query.first() is not None:
        if User.query.filter_by(email=Config.ADMIN_EMAIL).first() is None:
            user = User(first_name='Admin',
                        last_name='Account',
                        password=Config.ADMIN_PASSWORD,
                        confirmed=True,
                        email=Config.ADMIN_EMAIL)
            db.session.add(user)
            db.session.commit()
            print('Added administrator {}'.format(user.full_name()))
    pasien_query = Role.query.filter_by(name='Pasien')
    if pasien_query.first() is not None:
        if User.query.filter_by(email='pasien@bara.my.id').first() is None:
            pasien = User(first_name='Pasien',
                          last_name='User',
                          password=Config.ADMIN_PASSWORD,
                          confirmed=True,
                          email='pasien@bara.my.id')
            db.session.add(pasien)
            db.session.commit()
            print('Added pasien {}'.format(pasien.full_name()))


@manager.command
def run_worker():
    """Initializes a slim rq task queue."""
    listen = ['default']
    redis_url = app.config['REDIS_URL']
    conn = Redis.from_url(redis_url)

    # conn = Redis(
    #     host=app.config['RQ_DEFAULT_HOST'],
    #     port=app.config['RQ_DEFAULT_PORT'],
    #     db=0,
    #     password=app.config['RQ_DEFAULT_PASSWORD'])

    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()


@manager.command
def format():
    """Runs the yapf and isort formatters over the project."""
    isort = 'isort -rc *.py app/'
    yapf = 'yapf -r -i *.py app/'

    print('Running {}'.format(isort))
    subprocess.call(isort, shell=True)

    print('Running {}'.format(yapf))
    subprocess.call(yapf, shell=True)


if __name__ == '__main__':
    manager.run()