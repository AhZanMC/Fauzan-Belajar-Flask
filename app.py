# Library
from flask import Flask, flash, render_template, request, redirect, url_for

# Buat Inisialisasi Aplikasi Flask
app = Flask(__name__)

## Ini Data Dummy buat testing
data_barang = [
    {"id": 1, "nama": "Laptop Asus ROG", "stok": 5, "harga": 15000000},
    {"id": 2, "nama": "Mouse Logitech", "stok": 10, "harga": 150000},
    {"id": 3, "nama": "Keyboard Mechanical", "stok": 5, "harga": 500000},
    {"id": 4, "nama": "Monitor Samsung 24 Inch", "stok": 7, "harga": 2000000},
    {"id": 5, "nama": "Mic Fantech Leviosa", "stok": 0, "harga": 2000000}
]

# Rute atau Jalur
@app.route('/')
def home():
    # return file html
    return render_template('index.html', barang=data_barang)

if __name__ == '__main__':
    app.run(debug=True)