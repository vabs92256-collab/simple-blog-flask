# setup_db.py
from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    
    db.create_all()
    
   
    if not User.query.filter_by(username='admin').first():
        admin_user = User(
            username='admin', 
            email='admin@problog.com', 
            is_admin=True
        )
        admin_user.set_password('Admin123!')
        db.session.add(admin_user)
        db.session.commit()
        print("--- Database Initialized Successfully ---")
        print("Admin Username: admin")
        print("Admin Password: Admin123!")
    else:
        print("Database already exists.")