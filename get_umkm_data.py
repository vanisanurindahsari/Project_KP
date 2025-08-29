import mysql.connector

def get_umkm_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db_dinas"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT tahun, jumlah_umkm FROM umkm")
    rows = cursor.fetchall()
    conn.close()

    years = [row[0] for row in rows]
    values = [row[1] for row in rows]

    return years, values
