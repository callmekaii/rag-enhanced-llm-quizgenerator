import gpt4all
from pdfprocessor import process_pdf

def initialize_model(model_path):
    model = gpt4all.GPT4All(model_path, model_type='gguf', 
                            allow_download=False,
                            device='gpu')
    return model

def generate_response(model, prompt, max_tokens=1000):
    response = model.generate(prompt, max_tokens=max_tokens)
    return response

#model declaration
model = initialize_model(r"D:\Github\rag-enhanced-llm-quizgen\.venv\LLM\Meta-Llama-3.1-8B-Instruct-128k-Q4_0.gguf")

try:
    path_to_pdf = r"D:\Github\rag-enhanced-llm-quizgen\.venv\PDF Sample\3.0 - Overview of Game Design.pdf"
    chunks = process_pdf(path_to_pdf)
    print(generate_response(model, "Make me a 10 questions quiz with 4 multiple choices from A-D with the info provided: "+chunks[0]))

except Exception as e:
    print("Error with file path:", e)

# print(generate_response(model, "Hello, what is 1+1?"))