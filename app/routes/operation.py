from flask import request, jsonify, session, Blueprint
from app import db
from app.models import User, Operation, Record
from app.services.operation_service import OperationService

operation_blueprint = Blueprint('operation', __name__)

@operation_blueprint.route('/operation', methods=['POST'])
def new_operation():
    data = request.get_json()
    user = User.query.get(session['user_id'])
    operation = Operation.query.get(data['operation_id'])
    
    if user.balance < operation.cost:
        return jsonify({'message': 'Insufficient balance.'}), 400
    
    amount = ",".join(str(x) for x in data['amount'])
    
    result = OperationService.perform_operation(operation.type, data['amount'])
    
    record = Record(user_id=user.id, operation_id=operation.id, amount=amount, user_balance=user.balance, operation_response=result)
    db.session.add(record)
    user.balance -= operation.cost
    db.session.commit()

    return jsonify({'response': result}), 200
