from pdfprocessor import process_pdf
#for instance query = writer in this case
def score_chunks(query = "game design"):
    query_terms = query.lower().split()  # multiple terms
    scored_chunks = []

    for chunk in chunks:
        score = 0
        split_chunk = chunk.lower().split()

        for term in query_terms:
            for word in split_chunk:
                # exact word match — you can make this fuzzy later if needed
                if word == term:
                    score += 10

        scored_chunks.append((chunk, score))

    return scored_chunks

def get_top_chunks(scored_chunks, top_n=5):
    scored_chunks.sort(key=lambda x: x[1], reverse=True)
    return scored_chunks[:top_n]

path_to_pdf = r"D:\Github\rag-enhanced-llm-quizgenerator\.venv\PDF Sample\3.0 - Overview of Game Design.pdf"
chunks = process_pdf(path_to_pdf)


scored_chunks = score_chunks()
sorted_top_chunks = get_top_chunks(scored_chunks)

#Debug function to print top chunks with scores
def debug_print_top_chunks(sorted_top_chunks):
    for i in range(len(sorted_top_chunks)):
        chunk_tuple = sorted_top_chunks[i]
        chunk = chunk_tuple[0]
        score = chunk_tuple[1]
        print(f"Chunk {i+1} (Score: {score}):\n{chunk}\n")


#Main function to get the best chunk
def get_best_chunk(sorted_top_chunks):
    # print("Best chunk: " + sorted_top_chunks[0][0])
    return sorted_top_chunks[0][0]

get_best_chunk(sorted_top_chunks)

