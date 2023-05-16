from app import db, create_app
from app.models.user import User

app = create_app()

with app.app_context():
    user = User.query.filter_by(username='test@example.com').first()

    # Check if user exists
    print(user.balance)
    if user:
        # Add balance to the user
        user.balance += 1000.0  # Add 100.0 to the user's balance

        # Save changes
        db.session.commit()