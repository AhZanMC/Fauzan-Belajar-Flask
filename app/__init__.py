from flask import Flask
from app.extensions import db # Import Ekstensi Database biar gak ribet

def create_app():
    app = Flask(__name__)
    
    # Konfigurasi database kamu (contoh SQLite)
    app.config['SECRET_KEY'] = 'bebas-isi-apa-aja-buat-session'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 2. Hubungkan db dengan app
    db.init_app(app)

    # 3. Import & register blueprint
    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    # 4. Import & register blueprint untuk main
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)

    return app