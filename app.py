from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PharmaEffect</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; background: #691b1b; color: white; }
        .container { max-width: 500px; margin: 50px auto; padding: 20px; background: #e2ceb1; border-radius: 15px; }
        input, button { margin-top: 10px; padding: 10px; width: 90%; border-radius: 5px; }
        button { background: #691b1b; color: white; cursor: pointer; }
        button:hover { background: #000000; }
    </style>
</head>
<body>
    <h1>PharmaEffect</h1>
    <div class="container">
        <h2>Skor Efektivitas Obat</h2>
        <form method="post">
            <input type="text" name="gejala" placeholder="Masukkan gejala..." required>
            <button type="submit">Cari Obat</button>
        </form>
        {% if hasil %}
            <p>{{ hasil }}</p>
            <p>{{ keterangan }}</p>
        {% endif %}
    </div>
</body>
</html>
"""

daftarObat = {
    "perut kembung": {"penyakit": "Gastritis", "obat": "Antasida, Omeprazole", "skor": 4.0},
    "mual": {"penyakit": "Gastritis", "obat": "Antasida, Omeprazole", "skor": 4.0},
    "sakit perut": {"penyakit": "Gastritis", "obat": "Antasida, Omeprazole", "skor": 4.0},
    "demam": {"penyakit": "Flu", "obat": "Paracetamol, Ibuprofen", "skor": 4.5},
    "batuk": {"penyakit": "Infeksi Saluran Pernapasan", "obat": "Dextromethorphan, Guaifenesin", "skor": 3.8}
}

def getKeteranganSkor(skor):
    if skor <= 1: return "Tidak efektif"
    if skor <= 2: return "Kurang efektif"
    if skor <= 3: return "Cukup efektif"
    if skor <= 4: return "Efektif"
    return "Sangat efektif"

@app.route('/', methods=['GET', 'POST'])
def index():
    hasil, keterangan = "", ""
    if request.method == 'POST':
        gejala = request.form['gejala'].lower()
        if gejala in daftarObat:
            data = daftarObat[gejala]
            hasil = f"Penyakit: {data['penyakit']}<br>Obat: {data['obat']}<br>Skor Efektivitas: {data['skor']}"
            keterangan = f"Kategori: {getKeteranganSkor(data['skor'])}"
        else:
            hasil = "Gejala tidak ditemukan. Konsultasikan dengan dokter."
    return render_template_string(HTML_TEMPLATE, hasil=hasil, keterangan=keterangan)

if __name__ == '__main__':
    app.run(debug=True)