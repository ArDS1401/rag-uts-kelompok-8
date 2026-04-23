# 🤖 RAG Starter Pack — UTS Data Engineering

> **Retrieval-Augmented Generation** — Sistem Tanya-Jawab Cerdas Berbasis Dokumen

Starter pack ini adalah **kerangka awal** proyek RAG untuk UTS Data Engineering D3/D4.
Mahasiswa mengisi, memodifikasi, dan mengembangkan kode ini sesuai topik kelompok masing-masing.

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

rag-uts-[nama-kelompok]/
│
├── data/  
│   ├── RP_Publish81525.pdf  
│   ├── dsultan,+10.+Andriani.pdf  
│   ├── jurnalppt,+Jurnal+Vol+4+No+2+Nas....pdf  
│   ├── sample_dokumen.txt  
│   └── share-of-global-plastic-waste-emitted....csv / txt  
│
├── src/  
│   ├── indexing.py        # Pipeline indexing  
│   ├── query.py           # Query & retrieval  
│   ├── embeddings.py      # Konfigurasi embedding  
│   └── utils.py           # Helper functions  
│
├── ui/  
│   └── app.py             # Streamlit UI  
│
├── docs/  
│   └── arsitektur.png     # Diagram arsitektur  
│
├── evaluation/  
│   └── hasil_evaluasi.xlsx  
│
├── notebooks/  
│   └── 01_demo_rag.ipynb  
│
├── .env.example  
├── .gitignore  
├── requirements.txt  
└── README.md  


## ⚡ Cara Memulai (Quickstart)

### 1. Clone & Setup

```bash
# Clone repository ini
git clone https://github.com/[username]/rag-uts-[kelompok].git
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
| `MODEL_NAME` | *(isi)* | Nama model LLM yang digunakan |

---

## 📊 Hasil Evaluasi

*(Isi setelah pengujian selesai)*

| # | Pertanyaan | Jawaban Sistem | Jawaban Ideal | Skor (1-5) |
|---|-----------|----------------|---------------|-----------|
| 1 | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... |

**Rata-rata Skor:** ...  
**Analisis:** ...

---

## 🏗️ Arsitektur Sistem

*(Masukkan gambar diagram arsitektur di sini)*

```
[Dokumen] → [Loader] → [Splitter] → [Embedding] → [Vector DB]
                                                         ↕
[User Query] → [Query Embed] → [Retriever] → [Prompt] → [LLM] → [Jawaban]
```

---

## 📚 Referensi & Sumber

- Framework: *(LangChain docs / LlamaIndex docs)*
- LLM: *(Groq / Gemini / Ollama)*
- Vector DB: *(ChromaDB / FAISS docs)*
- Tutorial yang digunakan: *(cantumkan URL)*

---

## 👨‍🏫 Informasi UTS

- **Mata Kuliah:** Data Engineering
- **Program Studi:** D4 Teknologi Rekayasa Perangkat Lunak
- **Deadline:** *24 April 2026*
