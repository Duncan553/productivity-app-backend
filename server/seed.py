from app import app
from models import db, User, Workout

with app.app_context():
    print("Clearing old data...")
    Workout.query.delete()
    User.query.delete()
    
    print("Creating test user...")
    u1 = User(username="trainer_joe")
    u1.password_hash = "password123"
    db.session.add(u1)
    db.session.commit() # Save user first to get an ID
    
    print("Creating test workout...")
    w1 = Workout(
        title="Monday Morning Cardio", 
        notes="Focus on heart rate stability", 
        user_id=u1.id
    )
    db.session.add(w1)
    db.session.commit()
    
    print("Seed complete! Database is ready.")
    print("Login with: trainer_joe / password123")
