import fill_DB
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Initialize the text splitter with chunk size and overlap
text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, 
                                               chunk_overlap=100, 
                                               length_function=len,
                                               is_separator_regex=False)

# Initialize empty lists to hold documents, ids, and metadata
documents = []
ids = []
metadatas = []

# Function to extract text from PDF
def extract_text_from_pdf(path):
    loader = PyPDFDirectoryLoader(path)
    raw_documents = loader.load()
    return raw_documents

# Function to split raw documents into chunks
def text_chunker(raw_documents):
    chunks = text_splitter.split_documents(raw_documents)
    return chunks

# Function to append the content to the lists
def append_contents_to_var(chunks):
    for i, chunk in enumerate(chunks):
        documents.append(chunk.page_content)
        ids.append(f"id_{i}")
        metadatas.append(chunk.metadata)
        # print(f"Metadata for chunk {i}: {chunk.page_content[:200]}...")  # Print first 50 characters of the chunk for reference

# Main processing flow
raw_documents = extract_text_from_pdf(r".venv/PDF Sample")  # Change the path to your PDF directory
chunks = text_chunker(raw_documents)  # Get the chunks from the raw documents
append_contents_to_var(chunks)  # Pass the chunks into the function

# Upsert the processed documents into the ChromaDB collection
fill_DB.collection.upsert(documents=documents,
                          metadatas=metadatas,
                          ids=ids)

print("PDF chunks have been processed and stored in ChromaDB.")
