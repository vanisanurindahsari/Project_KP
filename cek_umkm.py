import mysql.connector

# Koneksi ke database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Ganti jika ada password MySQL
    database="db_dinas"
)

cursor = db.cursor()

# Query untuk menghitung UMKM Aktif
cursor.execute("SELECT COUNT(*) FROM umkm WHERE status = 'Aktif'")
hasil = cursor.fetchone()

# Tampilkan hasil
print("Total UMKM Aktif:", hasil[0])

# Tutup koneksi
cursor.close()
db.close()
