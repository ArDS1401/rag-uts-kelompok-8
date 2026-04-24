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

| # | Pertanyaan | Jawaban Sistem | Jawaban Ideal | Skor |
|---|-----------|----------------|---------------|------|
| 1 | Sampah laut itu sebenarnya paling banyak jenis apa sih di daerah Makassar? | Berdasarkan data Pantai Tanjung Bayang, jenis terbanyak adalah *puntung rokok* (32,22% dan 0,88/m²). | Berdasarkan penelitian di Makassar, sampah paling dominan adalah plastik (70–80%) seperti kantong plastik, botol, dan fragmen plastik. | 3 |
| 2 | Kenapa plastik sering banget jadi sampah yang paling dominan di laut? | Plastik dominan karena mudah terbawa arus dan merupakan jenis sampah yang paling umum ditemukan. | Plastik dominan karena sulit terurai (persistent), penggunaan tinggi, dan pengelolaan limbah yang kurang baik. | 4 |
| 3 | Sampah di laut itu asalnya dari mana aja sih? | Sampah berasal dari aktivitas manusia di darat dan laut (antropogenik). | ±80% berasal dari darat (limbah rumah tangga, industri, sungai) dan sisanya dari aktivitas laut (kapal, perikanan, budidaya). | 4 |
| 4 | Kok bisa ya sampah numpuk di satu tempat tertentu di pantai atau pulau? | Sampah menumpuk karena:<br>1. Terbawa arus & ombak<br>2. Buangan domestik<br>3. Aktivitas manusia<br>4. Karakteristik sampah | Disebabkan arus laut dan angin yang membawa sampah lalu terjebak di area sirkulasi lambat (teluk/hotspot). | 5 |
| 5 | Sampah laut itu berbahaya nggak sih buat ikan dan kehidupan laut lainnya? | Ya, berbahaya dan merusak ekosistem serta habitat laut. | Dampak:<br>- Entanglement (terjerat)<br>- Ingestion (tertelan)<br>- Mikroplastik masuk rantai makanan | 4 |
| 6 | Gimana sih cara peneliti ngukur banyaknya sampah di pantai atau laut? | Metode:<br>1. Observasi saat surut<br>2. Form CSIRO<br>3. Kategorisasi sampah | Metode transek:<br>- Area ±100 m<br>- Hitung item/m²<br>- Berat (g/m²) | 5 |
| 7 | Apa bedanya sampah makro sama sampah meso? | Perbedaan pada ukuran (meso disaring 0,5 cm, makro lebih besar). | Makro > 2,5 cm<br>Meso 0,5–2,5 cm | 4 |
| 8 | Kenapa daerah yang banyak aktivitas manusia sampahnya lebih banyak? | Karena jumlah penduduk, aktivitas, dan konsumsi tinggi serta wisata. | Karena kepadatan penduduk, aktivitas tinggi, dan keterbatasan pengelolaan sampah (TPA). | 5 |
| 9 | Orang-orang di sekitar pesisir biasanya mengelola sampahnya gimana sih? | Umumnya dibuang langsung ke laut. | Selain dibuang ke laut, juga dibakar karena keterbatasan fasilitas pengelolaan sampah. | 4 |
| 10 | Solusi paling penting buat ngurangin sampah laut itu apa? | Partisipasi masyarakat sangat penting. | Solusi:<br>- Infrastruktur pengelolaan<br>- Edukasi masyarakat<br>- Teknologi (trash trap) | 4 |

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
