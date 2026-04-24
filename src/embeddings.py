"""
=============================================================
MODUL EMBEDDING — RAG UTS Data Engineering
=============================================================
File ini digunakan untuk membuat fungsi yang menyimpan model
untuk Embedding.
=============================================================
"""

from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embedding_model():
    """
    Mengembalikan instance model embedding HuggingFace yang sudah dikonfigurasi.
    """
    return HuggingFaceEmbeddings(
        model_name= "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        model_kwargs={"device": "cpu"}
    )