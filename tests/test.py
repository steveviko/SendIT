import json
import pytest
from app import create_app
from app.database.models import Database
from app.database.dboperations import DbOperations
from tests import test_base



# creating our test client
@pytest.fixture(scope='module')
def client():
    app = create_app()
    test_client = app.test_client()

    # creating the database object
    database = Database()
    database.create_user_table()
    database.create_parcels_table()
    # establishing the application context
    cxt = app.app_context()
    cxt.push()
    yield test_client
    database.drop_tables()
    cxt.pop()


@pytest.fixture
def dboperations(scope="module"):
    dboperations_object = DbOperations()
    yield dboperations_object


def test_register_user(dboperations):
    create_user = {
        "username":"steve",
        "hash_password": "password",
        "email": "email@email",
        "role":"user"
    }
    assert dboperations.add_user(create_user)   

def test_fecth_user_by_id(dboperations):
    user_id = 5
    assert dboperations.fetch_user_by_id(user_id) == None
    assert not isinstance(dboperations.fetch_user_by_id(user_id), tuple)

def test_fecth_user_email(dboperations):
    email = "steveb@mail.com"
    assert dboperations.fetch_user_email(email) == None
    assert not isinstance(dboperations.fetch_user_email(email), tuple)

def test_login_user_is_invalid(dboperations): 
    username=None
    assert not isinstance(dboperations.query_username(
            username), tuple)
          
