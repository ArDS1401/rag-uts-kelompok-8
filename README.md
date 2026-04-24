# 🤖 RAG Starter Pack — UTS Data Engineering

> **Retrieval-Augmented Generation** — Sistem Tanya-Jawab Cerdas Berbasis Dokumen

Permasalahan pencarian informasi berbasis dokumen sering kali membutuhkan waktu lama dan tidak efisien ketika data tidak terstruktur. Oleh karena itu, projek ini mengimplementasikan **Retrieval-Augmented Generation (RAG)** untuk membangun sistem tanya jawab berbasis dokumen dengan studi kasus Sampah Laut.

---

👥 Identitas Kelompok

| Nama | NIM | Tugas Utama |
|------|-----|-------------|
| Arie Dwi Sulistyo | 244311004 | Project Manager  |
| Dila Alif Regita  | 244311010 | Data Analyst         |
| Suqya Rohmatin  | 244311028 | Data Engineer         |

**Topik Domain:** *Sampah Laut*  
**Stack yang Dipilih:** *LangChain*  
**LLM yang Digunakan:** *Gemini*  
**Vector DB yang Digunakan:** *ChromaDB*

---

## 📁 Struktur Proyek

```text
rag-uts-kelompok-8/
├── data/
│   ├── RP_Publish81525.pdf
│   ├── dsultan,+10.+Andriani.pdf
│   ├── jurnalppt,+Jurnal+Vol+4+No+2+Nas....pdf
│   ├── dampak_sampah_laut.csv
│   ├── jenis_sampah_laut.csv
│   ├── klasifikasi_ukuran_sampah_laut.csv
│   └── sumber_sampah_laut.csv
├── assets/
│   └── Arsitektur.jpeg
├── src/
│   ├── indexing.py        # Pipeline indexing
│   ├── query.py           # Query & retrieval
│   ├── embeddings.py      # Konfigurasi embedding
│   └── utils.py           # Helper functions
├── ui/
│   └── app.py             # Streamlit UI
├── docs/
│   └── arsitektur.png     # Diagram arsitektur
├── evaluation/
    └──Evaluasi_Sistem.xlsx
│   └── hasil_evaluasi.xlsx
├── notebooks/
│   └── 01_demo_rag.ipynb
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```
## ⚡ Cara Memulai (Quickstart)

### 1. Clone & Setup

```bash
# Clone repository ini
git clone https://github.com/ArDS1401/rag-uts-kelompok8.git
cd rag-uts-[kelompok]

# Buat virtual environment
python -m venv venv
source venv/bin/activate        # Linux/Mac
# atau: venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

### 2. Konfigurasi API Key

```bash
# Salin template env
cp .env.example .env

# Edit .env dan isi API key Anda
# JANGAN commit file .env ke GitHub!
```

### 3. Siapkan Dokumen

Letakkan dokumen sumber Anda di folder `data/`:
```bash
# Contoh: salin PDF atau TXT ke folder data
cp dokumen-saya.pdf data/
```

### 4. Jalankan Indexing (sekali saja)

```bash
python src/indexing.py
```

### 5. Jalankan Sistem RAG

```bash
# Dengan Streamlit UI
streamlit run ui/app.py

# Atau via CLI
python src/query.py
```

---

## 🔧 Konfigurasi

Semua konfigurasi utama ada di `src/config.py` (atau langsung di setiap file):

| Parameter | Default | Keterangan |
|-----------|---------|------------|
| `CHUNK_SIZE` | 500 | Ukuran setiap chunk teks (karakter) |
| `CHUNK_OVERLAP` | 50 | Overlap antar chunk |
| `TOP_K` | 3 | Jumlah dokumen relevan yang diambil |
| `MODEL_NAME` | Gemini 3 Flash | Model AI yang digunakan untuk menjawab pertanyaan dengan  cepat dan mudah |

---

## 📊 Hasil Evaluasi

*(Isi setelah pengujian selesai)*

| # | Pertanyaan | Jawaban Sistem | Jawaban Ideal | Skor (1-5) |
|---|-----------|----------------|---------------|-----------|
| 1 | Sampah laut itu sebenarnya paling banyak jenis apa sih di daerah Makassar? | Berdasarkan data di Pantai Tanjung Bayang (Kota Makassar) untuk ukuran 5 mm – 2,5 cm, jenis sampah laut yang paling banyak adalah *puntung rokok* (PL11) dengan persentase berat sebesar 32,22% dan jumlah 0,88 per m². | Berdasarkan data penelitian di perairan Makassar (seperti di Pulau Barrang Lompo dan sekitarnya), jenis sampah yang paling mendominasi adalah Plastik. Data menunjukkan bahwa plastik menyumbang persentase terbesar, yaitu sekitar 70% hingga 80% dari total sampah yang ditemukan. Komposisi spesifiknya meliputi kantong plastik, botol minuman, dan potongan plastik (fragmen). | 2 |
| 2 | Kenapa plastik sering banget jadi sampah yang paling dominan di laut? | Berdasarkan konteks tersebut, plastik menjadi sampah yang dominan karena mudah terbawa oleh arus laut dari daratan utama maupun tempat lain. Selain itu, sampah plastik merupakan jenis sampah yang paling umum dan banyak dijumpai di seluruh perairan dunia. | Plastik mendominasi karena sifat materialnya yang tahan lama (persistent) dan sulit terurai secara biologis, sehingga menumpuk selama puluhan tahun. Selain itu, ketergantungan masyarakat pada kemasan plastik sekali pakai dan manajemen limbah yang kurang optimal menyebabkan plastik mudah terlepas ke lingkungan laut dalam jumlah besar. | 4 |
| 3 | Sampah di laut itu asalnya dari mana aja sih, apakah cuma dari laut atau dari darat juga? | Sampah laut berasal dari aktivitas manusia di darat yang dibuang secara langsung maupun tidak langsung ke laut, serta dihasilkan dari kegiatan antropogenik. | Aktivitas Daratan (Land-based): Sumber terbesar (sekitar 80%), yang berasal dari buangan pemukiman, limbah industri, dan sampah wisata yang terbawa aliran sungai atau sistem drainase menuju laut. Aktivitas Laut (Sea-based): Berasal dari kegiatan penangkapan ikan (jaring yang terbuang), operasional kapal transportasi, serta kegiatan budidaya laut (seperti pelampung plastik). | 4 |
| 4 | Kok bisa ya sampah numpuk di satu tempat tertentu di pantai atau pulau? | Sampah menumpuk di pantai atau pulau disebabkan oleh:1.  *Terbawa arus dan ombak:* Sampah mengapung terbawa oleh arus atau ombak laut dan terdeposit di pesisir, terutama saat air laut surut terendah. 2.  *Buangan domestik:* Masyarakat membuang sampah rumah tangga secara langsung ke laut. 3.  *Aktivitas manusia:* Adanya aktivitas di lokasi tertentu seperti kawasan wisata dan tempat perawatan kapal. 4.  *Karakteristik sampah:* Sampah dengan massa jenis tertentu atau kategori plastik yang mendominasi cenderung berkumpul dan menumpuk di wilayah pesisir.
 | Fenomena ini disebabkan oleh faktor fisik laut, yaitu arus permukaan dan angin. Sampah terbawa oleh arus dari daratan atau laut lepas, kemudian terjebak di daerah dengan sirkulasi air yang lambat, seperti teluk atau sisi pulau yang menghadap arah datangnya arus dominan (misal saat Musim Barat). Hal ini menciptakan zona akumulasi (hotspots) sampah. | 3 |
| 5 | Sampah laut itu berbahaya nggak sih buat ikan dan kehidupan laut lainnya? | Ya, sangat berbahaya. Sampah laut dapat menyebabkan kerusakan ekologi seperti peningkatan derajat keasaman, pemutihan karang, serta merupakan ancaman langsung terhadap habitat laut. Sampah plastik secara spesifik merupakan jenis yang paling berisiko memberikan dampak buruk pada organisme laut. | Sangat berbahaya. Dampaknya meliputi:
Entanglement: Biota laut (seperti penyu) terjerat jaring atau tali plastik yang menyebabkan luka fisik atau kematian.
Ingestion: Ikan dan mamalia laut mengira plastik adalah makanan (seperti ubur-ubur). Plastik yang tertelan tidak dapat dicerna, menyumbat organ dalam, dan menyebabkan kematian akibat kelaparan.
Mikroplastik: Plastik yang terpecah menjadi butiran kecil dapat masuk ke dalam jaringan tubuh ikan dan berpotensi masuk ke rantai makanan manusia.
 | 5 |
| 6 | Gimana sih cara peneliti ngukur banyaknya sampah di pantai atau laut? | Peneliti mengukur banyaknya sampah di pantai dengan cara:
1.  *Metode Pengamatan:* Dilakukan pada saat air laut surut terendah di daerah intertidal.
2.  *Instrumen Data:* Menggunakan formulir CSIRO (Commonwealth Scientific and Industrial Research Organization).
3.  *Kategorisasi:* Sampah dikelompokkan berdasarkan jenis bahannya, seperti plastik keras, plastik lunak, tali plastik, logam, kaca, karet, busa, kain, kayu, kertas/kardus, dan lainnya.
 | Peneliti menggunakan metode Monitoring Sampah Pantai dengan teknik sampling:
Menentukan area (transek) tertentu, biasanya berukuran 100 meter sepanjang garis pantai.
Mengumpulkan seluruh sampah di dalam area tersebut.
Menghitung kelimpahan (jumlah item per meter persegi, $item/m^2$) dan berat sampah per satuan luas ($g/m^2$). | 5 |
| 7 | Apa bedanya sampah makro sama sampah meso yang disebut di penelitian itu? | Berdasarkan teks tersebut, perbedaan sampah makro dan meso terletak pada ukurannya. Sampah meso diidentifikasi menggunakan saringan 0,5 cm, sedangkan sampah makro merupakan kategori ukuran sampah yang lebih besar, namun batas ukuran spesifik untuk makro tidak disebutkan secara detail dalam dokumen tersebut. | Perbedaannya terletak pada ukuran dimensinya sesuai standar klasifikasi:
Sampah Makro (Macro-debris): Sampah yang berukuran > 2,5 cm (contoh: botol, sandal, kemasan deterjen).
Sampah Meso (Meso-debris): Sampah yang berukuran antara 0,5 cm sampai 2,5 cm (contoh: fragmen plastik kecil, puntung rokok, atau tutup botol kecil).
 | 4 |
| 8 | Kenapa daerah yang banyak aktivitas manusia (kayak wisata atau permukiman) sampahnya lebih banyak? | Besarnya sampah yang dihasilkan di suatu daerah sebanding dengan jumlah penduduk, jenis aktivitas yang beragam, dan tingkat konsumsi penduduk tersebut terhadap barang material. Selain itu, aktivitas wisata yang tinggi juga memicu penumpukan sampah yang lebih banyak di suatu kawasan. | Terdapat korelasi positif antara kepadatan penduduk dan jumlah sampah. Semakin banyak aktivitas (seperti pemukiman padat atau objek wisata), semakin tinggi volume limbah domestik yang dihasilkan. Di lokasi seperti Pantai Losari atau Pulau yang berpenduduk padat, keterbatasan lahan untuk TPA (Tempat Pembuangan Akhir) seringkali membuat warga membuang sampah langsung ke perairan. | 5 |
| 9 | Orang-orang di sekitar pesisir biasanya mengelola sampahnya gimana sih? | Berdasarkan konteks, masyarakat di wilayah pesisir atau pulau (seperti Pulau Lae-Lae) cenderung mengelola sampah dengan cara membuangnya langsung ke laut. | Berdasarkan studi kasus di beberapa pulau di Makassar, pengelolaan sampah masih menjadi tantangan besar. Banyak masyarakat yang masih membakar sampah secara terbuka atau membuangnya langsung ke laut (khususnya saat air pasang) karena tidak adanya sistem pengangkutan sampah yang rutin dari pulau ke daratan utama. | 4 |
| 10 | Dari data yang ada, kira-kira solusi paling penting buat ngurangin sampah laut itu apa? | Berdasarkan data tersebut, solusi paling penting untuk mengurangi sampah laut adalah partisipasi masyarakat, karena tanpa partisipasi masyarakat, kesinambungan pengelolaan sampah sulit tercapai. | Solusi paling krusial meliputi:
Penguatan Infrastruktur: Penyediaan tempat sampah dan sistem pengangkutan sampah yang menjangkau pulau-pulau kecil.
Edukasi Perubahan Perilaku: Sosialisasi bahaya sampah plastik bagi ekosistem dan kesehatan.
Teknologi Penghalang (Trash Trap): Memasang jaring penahan sampah di muara sungai agar sampah dari daratan tidak sampai masuk ke perairan laut terbuka.
 | 4 |

**Rata-rata Skor:**  4.2 
**Analisis:** Sistem saat ini masih memiliki keterbatasan dalam melakukan sintesis data makro karena jawaban yang dihasilkan cenderung terlalu berfokus pada lokasi penelitian spesifik. Selain itu, akurasi parameter teknis terkait klasifikasi ukuran sampah (Meso vs Makro) serta pendalaman aspek ilmiah, seperti persistensi material plastik masih perlu ditingkatkan.

---

## 🏗️ Arsitektur Sistem

<img width="3353" height="7885" alt="Data Ingestion to Query-2026-04-24-014726" src="https://github.com/user-attachments/assets/e575b709-92b5-49a5-8bf7-6aea7450107d" />


```
[Dokumen] → [Loader] → [Chunking] → [Embedding] → [Vector DB]
                                      ↕
[User Query] → [Query Embed] → [Retriever] → [Prompt] → [LLM (Gemini)] → [Jawaban]
---

## 📚 Referensi & Sumber

- Framework: LangChain docs
- LLM: Gemini 
- Vector DB: ChromaDB 
- Tutorial yang digunakan: (cantumkan URL)

---

## 👨‍🏫 Informasi UTS

- **Mata Kuliah:** Data Engineering
- **Program Studi:** D4 Teknologi Rekayasa Perangkat Lunak
- **Deadline:** *Kamis, 23 April 2026*
