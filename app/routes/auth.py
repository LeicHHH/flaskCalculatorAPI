from flask import request, jsonify, session, Blueprint, current_app, json
from werkzeug.security import check_password_hash
from flask_sqlalchemy import SQLAlchemy
from app.models import User
import secrets

db = SQLAlchemy()

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()

    if user and check_password_hash(user.password, data['password']):
        session['user_id'] = user.id
        return jsonify({'message': 'Logged in successfully.', 'user': str(user.id)}), 200

    return jsonify({'message': 'Invalid credentials.'}), 401

@auth_blueprint.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully.'}), 200