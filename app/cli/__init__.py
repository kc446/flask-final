import os
import click
from flask.cli import with_appcontext
from app.db import db


@click.command(name='create-db')
@with_appcontext
def create_database():
    """Duh?"""
    # get root directory of project
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the app's database folder to database
    dbdir = os.path.join(root, '../database')
    # make a directory if it doesn't exist
    if not os.path.exists(dbdir):
        os.mkdir(dbdir)
    db.create_all()