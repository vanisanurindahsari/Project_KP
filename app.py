from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    total_aktif = 25
    return render_template('dashboard.html', total_aktif=total_aktif)

@app.route('/umkm-aktif')
def umkm_aktif():
    return "Halaman UMKM Aktif"

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/umkm-aktif')
def umkm_aktif():
    # Dummy data dulu (bisa nanti ambil dari database)
    data_umkm = [
        {"nama": "UMKM Sari Rasa", "jenis": "Kuliner"},
        {"nama": "UMKM Karya Mandiri", "jenis": "Kerajinan"},
        {"nama": "UMKM Berkah Jaya", "jenis": "Fashion"}
    ]
    return render_template("umkm_aktif.html", data_umkm=enumerate(data_umkm))
