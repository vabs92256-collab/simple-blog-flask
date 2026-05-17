from flask import Flask, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        flash('Admin access required.', 'danger')
        return redirect(url_for('main.home'))

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    
    from app.auth.routes import auth
    from app.main.routes import main
    app.register_blueprint(auth)
    app.register_blueprint(main)

   
    from app.models import User, Post
    admin = Admin(app, name='Blog Admin', index_view=MyAdminIndexView())
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Post, db.session))

    return app