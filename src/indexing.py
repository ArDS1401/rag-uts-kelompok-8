"""
=============================================================
PIPELINE INDEXING — RAG UTS Data Engineering
=============================================================

Pipeline ini dijalankan SEKALI untuk:
1. Memuat dokumen dari folder data/
2. Memecah dokumen menjadi chunk-chunk kecil
3. Mengubah setiap chunk menjadi vektor (embedding)
4. Menyimpan vektor ke dalam vector database

Jalankan dengan: python src/indexing.py
=============================================================
"""

import os
import tabula
import pandas as pd
from pathlib import Path
from embeddings import get_embedding_model
from langchain_core.documents import Document
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

# ─── LANGKAH 0: Konfigurasi Path Lokal ───────────────────────────────────────
# Mengambil lokasi direktori tempat script ini berada
BASE_DIR = Path(__file__).resolve().parent

CHUNK_SIZE    = 500
CHUNK_OVERLAP = 50
DATA_DIR      = BASE_DIR / "../data"
VS_DIR        = BASE_DIR / "../vectorstore"

def etlPdf(pdf_path):
    """
    Fungsi untuk membongkar tabel di PDF dan mengubahnya menjadi teks naratif.
    """
    dokumen_tabel = []
    print(f"Mengekstrak tabel dari: {pdf_path.name}...")

    try:
        daftar_tabel = tabula.read_pdf(str(pdf_path), pages='all', multiple_tables=True, silent=True)

        for i, df in enumerate(daftar_tabel):
            df = df.dropna(how='all')

            for index, row in df.iterrows():
                narasi = f"Data statistik dari {pdf_path.name} pada tabel {i+1}: "
                detil_baris = ", ".join([f"{col} adalah {row[col]}" for col in df.columns if pd.notna(row[col])])
                narasi += detil_baris + "."

                doc = Document(
                    page_content=narasi,
                    metadata={"source": str(pdf_path.name), "page": "tabel_ekstraksi"}
                )
                dokumen_tabel.append(doc)

    except Exception as e:
        print(f"Gagal mengekstrak tabel di {pdf_path.name}: {e}")

    return dokumen_tabel

def build_index_langchain():
    print("=" * 50)
    print("Memulai Pipeline Indexing (Versi Lokal)")
    print("=" * 50)

    # Pastikan folder data ada
    if not DATA_DIR.exists():
        print(f"Error: Folder '{DATA_DIR.name}' tidak ditemukan di {BASE_DIR}")
        print("Silakan buat folder 'data' dan masukkan file PDF/CSV ke dalamnya.")
        return None

    # ─── LANGKAH 1: Load Dokumen (Teks + Tabel + CSV) ──────────
    print("\n Langkah 1: Memuat dokumen...")

    loader_pdf = DirectoryLoader(
        str(DATA_DIR),
        glob="**/*.pdf",
        loader_cls=PyPDFLoader,
        show_progress=True,
        silent_errors=True
    )
    documents_pdf = loader_pdf.load()

    docs_tables = []
    for file_pdf in DATA_DIR.glob("**/*.pdf"):
        hasil = etlPdf(file_pdf)
        docs_tables.extend(hasil)

    print("   Memuat data dari file CSV...")
    loader_csv = DirectoryLoader(
        str(DATA_DIR),
        glob="**/*.csv",
        loader_cls=CSVLoader,
        loader_kwargs={"encoding": "utf-8"},
        show_progress=True
    )
    documents_csv = loader_csv.load()

    all_docs = documents_pdf + docs_tables + documents_csv

    print(f"   {len(documents_pdf)} halaman teks PDF dimuat.")
    print(f"   {len(docs_tables)} baris data tabel PDF dikonversi.")
    print(f"   {len(documents_csv)} baris data CSV dimuat.")
    print(f"   Total dokumen yang akan diproses: {len(all_docs)}")

    if len(all_docs) == 0:
        print(f"   PERINGATAN: Tidak ada data ditemukan di {DATA_DIR}!")
        return None

    # ─── LANGKAH 2: Chunking ─────────────────────────────────
    print(f"\nLangkah 2: Memecah dokumen...")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    chunks = splitter.split_documents(all_docs)
    print(f"   {len(chunks)} chunk berhasil dibuat.")

    # ─── LANGKAH 3: Embedding ────────────────────────────────
    print("\nLangkah 3: Membuat embedding (model multilingual)...")
    embedding_model = get_embedding_model()

    # ─── LANGKAH 4: Simpan ke Vector DB ──────────────────────
    print(f"\nLangkah 4: Menyimpan ke ChromaDB...")
    VS_DIR.mkdir(parents=True, exist_ok=True)

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=str(VS_DIR)
    )

    print("\n" + "=" * 50)
    print(f"Indexing selesai! Vector database tersimpan di: {VS_DIR}")
    print("=" * 50)

    return vectorstore

if __name__ == "__main__":
    build_index_langchain()