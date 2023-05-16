import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from flask_login import login_user
from app import create_app, db
from app.models import User, Operation, Record

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_user_and_operation(client):
    # Create a user and operation for testing
    with client.application.app_context():
        user = User(id=1, username='test@example.com', password='password123', balance=20, status='active')
        operation = Operation(id=1, type='addition', cost=1)
        db.session.add(user)
        db.session.add(operation)
        db.session.commit()
        
        assert User.query.get(1) is not None
        assert Operation.query.get(1) is not None
