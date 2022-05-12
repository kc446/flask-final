import os

from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy

from app import config

db = SQLAlchemy()
database = Blueprint('database', __name__)

def get_db():
    """Connect to the application's configured database.
    The connection is unique for each request and will be reused if this is called again."""
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    """If this request connected to the database, close the connection."""
    db = g.pop("db", None)
    if db is not None:
        db.close()

@database.cli.command('create')
def init_db():
    db.create_all()

@database.before_app_first_request
def create_db_file_if_does_not_exist():
    root = config.Config.BASE_DIR
    # set the name of the apps log folder to logs
    dbdir = os.path.join(root,'..',config.Config.DB_DIR)
    # make a directory if it doesn't exist
    if not os.path.exists(dbdir):
        os.mkdir(dbdir)
    db.create_all()

@database.before_app_first_request
def create_upload_folder():
    root = config.Config.BASE_DIR
    # set the name of the apps log folder to logs
    uploadfolder = os.path.join(root,'..',config.Config.UPLOAD_FOLDER)
    # make a directory if it doesn't exist
    if not os.path.exists(uploadfolder):
        os.mkdir(uploadfolder)
    db.create_all()