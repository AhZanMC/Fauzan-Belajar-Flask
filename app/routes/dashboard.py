from flask import Blueprint, render_template, redirect, url_for, session

dashboard_bp = Blueprint('dashboard', __name__)

# Dashboard Blueprint buat halaman utama setelah login > dilempar ke dashboard :v
@dashboard_bp.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    return render_template('index.html', username=session.get('username'))