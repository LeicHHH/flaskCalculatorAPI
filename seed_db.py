from app import db, create_app
from app.models.operation import Operation
from app.models.user import User
from werkzeug.security import generate_password_hash
app = create_app()

with app.app_context():
    db.create_all()

    # Creating operation types and their costs
    operations = [
        Operation(type='addition', cost=10.0),
        Operation(type='subtraction', cost=10.0),
        Operation(type='multiplication', cost=15.0),
        Operation(type='division', cost=15.0),
        Operation(type='square_root', cost=20.0),
        Operation(type='random_string', cost=25.0)
    ]

    # Creating a testing user
    testing_user = User(username='test@example.com', password=generate_password_hash('password123'), status='active', balance=500.0)

    # Adding operations and testing user to the session
    for operation in operations:
        db.session.add(operation)
    
    db.session.add(testing_user)

    # Committing the session to the database
    db.session.commit()