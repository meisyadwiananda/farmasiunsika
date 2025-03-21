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
    "batuk": {"penyakit": "Infeksi Saluran Pernapasan", "obat": "Dextromethorphan, Guaifenesin", "skor": 4.2},
    "batuk kering": {"penyakit": "Iritasi tenggorokan", "obat": "Dextromethorphan, Antihistamin", "skor": 4.1},
    "batuk berdahak": {"penyakit": "Infeksi saluran pernapasan", "obat": "Guaifenesin, Bromhexine", "skor": 4.3},
    "pilek": {"penyakit": "Flu", "obat": "Antihistamin, Dekongestan", "skor": 4.0},
    "sakit kepala": {"penyakit": "Migrain", "obat": "Paracetamol, Ibuprofen", "skor": 4.3},
    "pusing": {"penyakit": "Vertigo", "obat": "Betahistine, Dimenhydrinate", "skor": 4.1},
    "nyeri sendi": {"penyakit": "Artritis", "obat": "Ibuprofen, Naproxen", "skor": 4.3},
    "nyeri otot": {"penyakit": "Cedera otot", "obat": "Paracetamol, Ibuprofen", "skor": 4.0},
    "sakit gigi": {"penyakit": "Infeksi gigi", "obat": "Ibuprofen, Asam Mefenamat", "skor": 4.4},
    "sakit tenggorokan": {"penyakit": "Radang tenggorokan", "obat": "Lozenges, Ibuprofen", "skor": 4.2},
    "mimisan": {"penyakit": "Iritasi hidung", "obat": "Oksimetazolin, Air garam", "skor": 3.8},
    "diare": {"penyakit": "Infeksi pencernaan", "obat": "Loperamide, Oralit", "skor": 4.3},
    "sembelit": {"penyakit": "Konstipasi", "obat": "Laksatif, Serat tambahan", "skor": 4.1},
    "asam lambung": {"penyakit": "GERD", "obat": "Omeprazole, Ranitidine", "skor": 4.4},
    "muntah": {"penyakit": "Mual", "obat": "Domperidone, Metoclopramide", "skor": 4.2},
    "gatal-gatal": {"penyakit": "Alergi", "obat": "Cetirizine, Loratadine", "skor": 4.3},
    "ruam kulit": {"penyakit": "Dermatitis", "obat": "Hidrokortison, Antihistamin", "skor": 4.0},
    "sesak napas": {"penyakit": "Asma", "obat": "Salbutamol, Kortikosteroid inhalasi", "skor": 4.5}
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