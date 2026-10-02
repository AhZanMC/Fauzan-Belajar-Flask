import os
from dotenv import load_dotenv
from flask import Flask
from models import db
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'default_fallback_key')

# Setup Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inisialisasi DB dengan App
db.init_app(app)

# Register Blueprint
app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)

# Buat tabel otomatis
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)