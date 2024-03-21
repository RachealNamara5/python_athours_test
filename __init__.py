from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from athours_app.controllers.auth_controllers import auth
from athours_app.extensions import db, migrate
from flask_bcrypt import Bcrypt
from athours_app.extensions import bcrypt
from athours_app.controllers.book_controllers import book




# db = SQLAlchemy()
# migrate = Migrate()



def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize SQLAlchemy and Flask-Migrate
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    # Import models
    from athours_app.models import user
    from athours_app.models import book
    from athours_app.models import company

    @app.route('/')
    def home():
        return "Hello programmers"
    
    #import blue prints
    from athours_app.controllers.auth_controllers import auth
    from athours_app.controllers.company_controllers import company
    from athours_app.controllers.book_controllers import book

    #register blue prints
    app.register_blueprint(auth,url_prefix='/api/v1/auth')
    app.register_blueprint(company,url_prefix='/api/v1/company')
    app.register_blueprint(book,url_prefix='/api/v1/book')


    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
