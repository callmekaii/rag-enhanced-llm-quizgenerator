import gpt4all
from pdfprocessor import process_pdf
from RAG_SemanticSearch import get_best_chunk, sorted_top_chunks

def initialize_model(model_path):
    model = gpt4all.GPT4All(model_path, model_type='gguf', 
                            allow_download=False,
                            device='gpu',)
    return model

def generate_response(model, prompt, max_tokens=1000):
    response = model.generate(prompt, max_tokens=max_tokens, n_batches=1024)
    return response

#model declaration
model = initialize_model(r"D:\Github\rag-enhanced-llm-quizgenerator\.venv\LLM\Meta-Llama-3.1-8B-Instruct-128k-Q4_0.gguf")
#VARK model learner type assessment quiz generation
# try:
#     # path_to_pdf = r"D:\Github\rag-enhanced-llm-quizgenerator\.venv\PDF Sample\3.0 - Overview of Game Design.pdf"
#     # chunks = process_pdf(path_to_pdf)
#     with model.chat_session(system_prompt='''You are an expert educational survey content generator. Your task is to create multiple-choice quiz questions strictly following the VARK learning style framework (Visual, Auditory, Read/Write, Kinesthetic). 

# INSTRUCTIONS:
# 1. Generate exactly **10 questions per text excerpt**.
# 2. For each question, provide **four options labeled A-D** corresponding to **one VARK style each**:
#    - Visual (V): Involves images, charts, diagrams, illustrations, or spatial reasoning.
#    - Auditory (A): Involves listening, spoken explanations, discussions, or audio-based cues.
#    - Read/Write (R): Involves reading, writing, notes, or text-based materials.
#    - Kinesthetic (K): Involves hands-on activities, simulations, experiments, or physical actions.
# 3. Each question must **clearly indicate the VARK style in parentheses**, like so: (Visual), (Auditory), etc.
# 4. Ensure that **each question is self-contained and answerable using only the text provided**.
# 5. Number the questions sequentially (1–10) and present the answers consistently in A-D format.
# 6. Do **not** mix styles in a single option — each option must correspond strictly to its style if mentioned.
# 7. The questions **must** be "what would you most likely do" type questions to assess learning preferences.
# 8. Output only in the format below (no extra commentary):

# EXAMPLE FORMAT:

# Question 1: You need to understand how the roles in a game design team work for a project. What would you most likely do?
# A. Draw a flowchart to visualize the roles (Visual)
# B. Listen to a discussion or recording about each role (Auditory)
# C. Read notes or write a summary of each role (Read/Write)
# D. Act out the roles in a mock simulation (Kinesthetic)

# Question 2: [Next question text]
# A. ...
# B. ...
# C. ...
# D. ...'''):
#         response = model.generate("Make me a 10 questions quiz with 4 multiple choices from A-D according to the order of VARK model with the info provided: "+get_best_chunk(sorted_top_chunks), max_tokens=3000)
#         print("Quiz Generation Response:\n", response)
# except Exception as e:
#     print("Error with file path:", e)


# print(generate_response(model, "Hello, what is 1+1?"))