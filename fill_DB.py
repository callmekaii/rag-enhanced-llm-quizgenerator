import chromadb

CHROMA_PATH = "chroma_db"  # Path to store ChromaDB data
chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = chroma_client.get_or_create_collection(name="PDF_chunks_collection")

