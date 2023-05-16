from flask import Blueprint, request, jsonify, session
from app import db
from app.models import Record, User

record_blueprint = Blueprint('record', __name__)

@record_blueprint.route('/record', methods=['GET'])
def get_records():
    user_id = session.get('user_id')
    if user_id is None:
        return jsonify({'message': 'User not logged in'}), 401
    records = Record.query.filter_by(user_id=user_id, is_deleted=False).all()

    return jsonify([record.to_dict() for record in records]), 200
    
@record_blueprint.route('/record/<int:id>', methods=['DELETE'])
def delete_record(id):
    record = Record.query.get(id)
    if record is None:
        return jsonify({'message': 'Record not found'}), 404
    record.is_deleted = True
    db.session.commit()
    return jsonify({'message': 'Record deleted'}), 200
