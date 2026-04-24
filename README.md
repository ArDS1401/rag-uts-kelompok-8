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
| 1 | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |
| 4 | ... | ... | ... | ... |
| 5 | ... | ... | ... | ... |
| 6 | ... | ... | ... | ... |
| 7 | ... | ... | ... | ... |
| 8 | ... | ... | ... | ... |
| 9 | ... | ... | ... | ... |
| 10 | ... | ... | ... | ... |

**Rata-rata Skor:** ...  
**Analisis:** ...

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
