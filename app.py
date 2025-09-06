from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Fungsi koneksi database
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",          # sesuaikan
        database="db_dinas"   # sesuaikan dengan nama database kamu
    )

# Dashboard utama (statistik ringkas)
@app.route('/')
def dashboard():
    total_aktif = 25
    izin_koperasi_disetujui = 23
    return render_template(
        'dashboard.html',
        total_aktif=total_aktif,
        izin_koperasi_disetujui=izin_koperasi_disetujui
    )

# Route koperasi disetujui (ambil data dari DB)
@app.route('/koperasi-disetujui')
def koperasi_disetujui():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT tahun, jumlah_disetujui FROM izin_koperasi")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("koperasi_disetujui.html", data=data)


@app.route('/umkm-aktif')
def daftar_umkm():
    # Dummy data dulu (bisa nanti ambil dari database)
    data_umkm = [
        {
            "nama": "Eka Ayu Fitri Anggraini",
            "nama_umkm": "Chessy Kitchen",
            "nik": "3525156905870002",
            "alamat": "Bulak Rukem Timur 2-A/42",
            "produk": "Boba drink, Burger & snack",
            "status": "Aktif"
        },

        {
            "nama": "Murtosiyah",
            "nama_umkm": "Depot Jeng Mur",
            "nik": "3578295211730001",
            "alamat": "Bulak Cumpat Barat no 23",
            "produk": "Makanan dan minuman",
            "status": "Aktif"
            },

            {"nama": "Rizka Ayu Wahyuningtyas",
            "nama_umkm": "Kamila Kitchen", 
            "nik": "3578294809900002",
            "alamat": "Bulak Cumpat Timur 1 no 4",
            "produk": "Aneka Makanan, Snack Box, dan minuman",
            "status": "Aktif"
            },

            {"nama": "Khuzaimah Rumiati",
            "nama_umkm": "LGS", 
            "nik": "3578296603750001",
            "alamat": "Bulak Cumpat Barat 5/58",
            "produk": "Lumpia Rebung",
            "status": "Aktif"
            },

            {"nama": "Retno Date Dianingsih",
            "nama_umkm": "Dapoer Balqis", 
            "nik": "3524065102840002",
            "alamat": "Bulak Rukem Timur 1-A Buntu No.1-A",
            "produk": "Makanan & Minuman",
            "status": "Aktif"
            },

            {"nama": "Gadis Permata Sari",
            "nama_umkm": "Dapoer Sae", 
            "nik": "3578125005940001",
            "alamat": "Bulak Setro Utara 1/6",
            "produk": "BAKSO",
            "status": "Aktif"
            },

            {"nama": "Titin Priyanti",
            "nama_umkm": "Juice Inyong", 
            "nik": "3578056504840001",
            "alamat": "Bulak Cumpat Srono 3 no 23",
            "produk": "jus, nasi bakar, ketupat sayur, es kopyor",
            "status": "Aktif"
            },

            {"nama": "Yuli Rachmawati",
            "nama_umkm": "Hanny Kitchen", 
            "nik": "3578104107890012",
            "alamat": "Bulak Setro 3 No 10 B",
            "produk": "Sosis Bakar",
            "status": "Aktif"
            },

            {"nama": "Ani Karlina",
            "nama_umkm": "Rayau Kitchen", 
            "nik": "3578296511780001",
            "alamat": "Bulak Rukem Timur 1/107",
            "produk": "KUE BASAH",
            "status": "Aktif"
            },

            {"nama": "Chusnul Chotimah",
            "nama_umkm": "Pawon Nafisa", 
            "nik": "3578106705810005",
            "alamat": "Bogorami 5-B/1",
            "produk": "jus buah,salad buah,kue kering,mie ayam",
            "status": "Aktif"
            },

            {"nama": "Sri Ernawati, SE.MM/Erna Totok",
            "nama_umkm": "Gerai Jeng E'eng", 
            "nik": "3578296806690001",
            "alamat": "Bulak Cumpat Timur 3/17",
            "produk": "Makanan",
            "status": "Aktif"
            },

            {"nama": "Fitriah Wahyu Lillah",
            "nama_umkm": "New Miago", 
            "nik": "3578105303900008",
            "alamat": "Bulak Cumpat 2 no 19",
            "produk": "Dimsum",
            "status": "Aktif"
            },

            {"nama": "Erma Pujiati",
            "nama_umkm": "Dimsum Alzacky", 
            "nik": "3578296609860001",
            "alamat": "Bulak Cumpat Timur II no. 4D",
            "produk": "Dimsum",
            "status": "Aktif"
            },

            {"nama": "Nur Hasanah",
            "nama_umkm": "Cemilan Alfika", 
            "nik": "3578295706840001",
            "alamat": "Bulak Kali Tinjang 2/22",
            "produk": "Makanan dan minuman",
            "status": "Aktif"
            },

            {"nama": "Luluk Ainiyah",
            "nama_umkm": "Cibuyam Suroboyo", 
            "nik": "3578295409880001",
            "alamat": "JL.Nambangan Perak 9",
            "produk": "kue kering dan minuman",
            "status": "Aktif"
            },

            {"nama": "Sufianto Arif",
            "nama_umkm": "Sego Soge", 
            "nik": "3578292807790002",
            "alamat": "JL.Larangan VII/93",
            "produk": "makanan",
            "status": "Aktif"
            },

            {"nama": "Sabilah",
            "nama_umkm": "Pang Kupang", 
            "nik": "3578296206920001",
            "alamat": "Jl. Sukolilo lor 1",
            "produk": "Makanan & Minuman",
            "status": "Aktif"
            },

            {"nama": "Maria Ulfa",
            "nama_umkm": "Es Teh MU", 
            "nik": "3578296512860002",
            "alamat": "Sukolilo lor GG 6 no 17",
            "produk": "Es teh & jasuke",
            "status": "Aktif"
            },

            {"nama": "Irma Suryani",
            "nama_umkm": "Dam Food", 
            "nik": "3578295608850001",
            "alamat": "Sukolilo Lor 3/23",
            "produk": "Makanan & Minuman",
            "status": "Aktif"
            },

            {"nama": "Mahfud Yahomsyah",
            "nama_umkm": "Monzie", 
            "nik": "3578290104800003",
            "alamat": "Sukolilo Gg 6 No.5",
            "produk": "Makanan & Minuman",
            "status": "Aktif"
            },


            {"nama": "Ifa",
            "nama_umkm": "Bakaran Dower", 
            "nik": "3578295405870001",
            "alamat": "Tambak Deres 3/17",
            "produk": "Bakso,cumi bakar",
            "status": "Aktif"
            },


            {"nama": "Arobiyah",
            "nama_umkm": "Kedai Nokia", 
            "nik": "3578296009820003",
            "alamat": "Tambak Deres No 8",
            "produk": "Jual es lumut, es teh, es kopyor",
            "status": "Aktif"
            },
    ]
    return render_template("umkm_aktif.html", data_umkm=data_umkm)

@app.route('/komoditas')
def komoditas():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Ambil data komoditas
        query = "SELECT id, nama_komoditas FROM komoditas ORDER BY id"
        cursor.execute(query)
        data = cursor.fetchall()

    except Exception as e:
        print("Error saat ambil data komoditas:", e)
        data = []

    finally:
        if cursor: cursor.close()
        if conn: conn.close()

    return render_template('komoditas.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
