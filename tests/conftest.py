"""This makes the test configuration setup"""
# pylint: disable=redefined-outer-name
import os

import pytest

from app import create_app, User
from app.db import db


@pytest.fixture()
def application():
    """This makes the app itself."""

    #os.environ['FLASK_ENV'] = 'development' # use this env if you want to see whats in the database
    os.environ['FLASK_ENV'] = 'testing' # you need to run this one in testing to pass on github

    application = create_app()
    #application.config.update(ENV="development")
    #application.config.update({"TESTING": True})

    with application.app_context():
        db.create_all()
        yield application
        db.session.remove()

@pytest.fixture()
def add_user(application):
    """Adds a new user record to the database."""
    with application.app_context():
        #new record
        user = User('keith@webizly.com', 'testtest')
        db.session.add(user)
        db.session.commit()

@pytest.fixture()
def client(application):
    """This makes the http client."""
    return application.test_client()

@pytest.fixture()
def runner(application):
    """This makes the task runner."""
    return application.test_cli_runner()
