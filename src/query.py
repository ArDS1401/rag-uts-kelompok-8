"""
=============================================================
PIPELINE QUERY — RAG UTS Data Engineering
=============================================================

Pipeline ini dijalankan setiap kali user mengajukan pertanyaan:
1. Ubah pertanyaan user ke vektor (query embedding)
2. Cari chunk paling relevan dari vector database (retrieval)
3. Gabungkan konteks + pertanyaan ke dalam prompt
4. Kirim ke LLM untuk mendapatkan jawaban

Jalankan CLI dengan: python src/query.py
=============================================================
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# Import model embedding dari file buatan kita sendiri
from embeddings import get_embedding_model

# ─── SETUP LOKAL ─────────────────────────────────────────────────────────────
# 1. Mengambil API Key dari file .env (lebih profesional & aman)
load_dotenv()

# 2. Konfigurasi Path Dinamis
BASE_DIR = Path(__file__).resolve().parent
VS_DIR   = BASE_DIR / "../vectorstore"

# 3. Konfigurasi Model (Gunakan versi yang stabil di API publik)
LLM_MODEL = "gemini-3-flash-preview" 
TOP_K     = 3

def load_vectorstore():
    """Memuat vector database menggunakan model embedding yang konsisten"""
    from langchain_community.vectorstores import Chroma

    if not VS_DIR.exists():
        raise FileNotFoundError(
            f" Vector store tidak ditemukan di '{VS_DIR}'.\n"
            "Jalankan dulu script indexing.py untuk membuat database!"
        )

    embedding_model = get_embedding_model()

    vectorstore = Chroma(
        persist_directory=str(VS_DIR),
        embedding_function=embedding_model
    )
    return vectorstore

def retrieve_context(vectorstore, question: str, top_k: int = TOP_K) -> list:
    """Mencari potongan dokumen yang paling relevan"""
    results = vectorstore.similarity_search_with_score(question, k=top_k)

    contexts = []
    for doc, score in results:
        contexts.append({
            "content": doc.page_content,
            "source": doc.metadata.get("source", "unknown"),
            "score": round(float(score), 4)
        })
    return contexts

def build_prompt(question: str, contexts: list) -> str:
    """Menyusun perintah untuk dikirim ke Gemini"""
    context_text = "\n\n---\n\n".join(
        [f"[Sumber: {c['source']}]\n{c['content']}" for c in contexts]
    )

    prompt = f"""Kamu adalah asisten cerdas yang membantu menjawab pertanyaan berdasarkan dokumen.

INSTRUKSI:
- Jawab HANYA berdasarkan konteks di bawah ini.
- Jika informasi tidak ada, katakan "Saya tidak tahu".
- Gunakan Bahasa Indonesia yang ringkas.
- Jangan membuat informasi yang tidak ada dan menghalu.

KONTEKS:
{context_text}

PERTANYAAN:
{question}

JAWABAN:"""
    return prompt

def get_answer_gemini(prompt: str) -> str:
    """Mengirim prompt ke Google Gemini menggunakan SDK terbaru"""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError(" API Key tidak ditemukan! Pastikan file .env sudah benar.")

    client = genai.Client(api_key=api_key)
    
    response = client.models.generate_content(
        model=LLM_MODEL,
        contents=prompt
    )
    return response.text

def answer_question(question: str, vectorstore) -> dict:
    """Fungsi utama penggerak RAG"""
    contexts = retrieve_context(vectorstore, question)
    prompt = build_prompt(question, contexts)
    
    print(" Gemini sedang berpikir...")
    answer = get_answer_gemini(prompt)

    return {
        "answer": answer,
        "contexts": contexts
    }

# ─── INTERFACE TERMINAL ────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("  SISTEM RAG LOKAL — Proyek UTS Kelompok 8")
    print("=" * 55)

    try:
        vs = load_vectorstore()
        print(" Database berhasil dimuat. Siap menjawab!\n")
    except Exception as e:
        print(f"{e}")
        import sys
        sys.exit()

    while True:
        query = input("\n❓ Tanya sesuatu (atau ketik 'keluar'): ").strip()

        if query.lower() in ["keluar", "exit", "q"]:
            print(" Program dihentikan. Terima Kasih.")
            break

        if not query: continue

        try:
            result = answer_question(query, vs)
            print("\n JAWABAN:")
            print(result["answer"])
            
            print("\n📚 SUMBER:")
            for i, ctx in enumerate(result["contexts"], 1):
                print(f"   [{i}] {ctx['source']} (Skor: {ctx['score']})")
        except Exception as e:
            print(f" Terjadi kesalahan: {e}")