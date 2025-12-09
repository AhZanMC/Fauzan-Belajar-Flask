# Library
from flask import Flask, flash, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Buat Inisialisasi Aplikasi Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inisialisasi Database
db = SQLAlchemy(app)

class Barang(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    stok = db.Column(db.Integer, nullable=False)
    harga = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Barang {self.nama}>'

# Rute atau Jalur
## Rute Home
@app.route('/')
def home():
    data_barang = Barang.query.all()
    return render_template('index.html', barang=data_barang)

## Rute Buat Nambah Data
@app.route('/tambah', methods=['POST'])
def tambah_barang():
    # Ambil data yang diketik user di form HTML
    nama_form = request.form['nama']
    stok_form = int(request.form['stok'])
    harga_form = float(request.form['harga'])

    # Bikin objek barang baru
    barang_baru = Barang(nama=nama_form, stok=stok_form, harga=harga_form)

    # Simpan ke database
    db.session.add(barang_baru) # Tambah ke antrian data ini bro
    db.session.commit()         # tolong simpan permanen SEKARANg

    return redirect(url_for('home'))

## Rute buat hapus data
@app.route('/hapus/<int:id>')
def hapus_barang(id):
    barang = Barang.query.get_or_404(id)

    # Hapus data dan simpan perubahan ke database
    db.session.delete(barang)
    db.session.commit()

    return redirect(url_for('home'))

## Update atau Edit Data
@app.route('/edit/<int:id>', methods=['GET','POST'])
def edit_barang(id):
    barang = Barang.query.get_or_404(id)

    if request.method == 'POST':
        # Ini kalo data disimpan
        barang.nama = request.form['nama']
        barang.stok = int(request.form['stok'])
        barang.harga = float(request.form['harga'])

        # Simpan perubahan ke database
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', barang=barang)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Buat tabel database jika belum ada
    app.run(debug=True)