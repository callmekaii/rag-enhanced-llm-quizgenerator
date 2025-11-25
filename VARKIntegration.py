import llmintegration
import RAG_SemanticSearch
#This is the part where VARK assessment is going to be implemented
Answers = [0, 0]
user_preference = ""
def VarkAssessment():
        # [Auditory count, Read/Write count]
        global user_preference
        global Answers
        for i in range(1, 11):
            while True:
                Answer = input(f"Please enter the correct answer for Question {i} (A or B): ")
                if Answer.upper() == 'A':
                    Answers[0] += 1
                    break
                elif Answer.upper() == 'B':
                    Answers[1] += 1
                    break
                else:
                    print("Invalid input. Please enter A or B.")
        if Answers[0] > Answers[1]:
            print(f"You prefer the Auditory learning style with {Answers[0]} out of 10 answers.")
            user_preference = "Auditory"
        elif Answers[1] > Answers[0]:
            print(f"You prefer the Read/Write learning style with {Answers[1]} out of 10 answers.")
            user_preference = "R/W"
        else:
            print(f"You have a balanced preference between Auditory and Read/Write learning styles with {Answers[0]} out of 10 answers each.")
            user_preference = "Balanced"

try:
    with llmintegration.model.chat_session(system_prompt='''
You are an expert educational survey content generator. Your task is to create multiple-choice quiz questions strictly following the VARK learning style framework (Auditory, Read/Write). 

INSTRUCTIONS:
1. Generate exactly **10 questions per text excerpt**.
2. For each question, provide **two options labeled A-B** corresponding to **one VARK style each**:
   - Auditory (A): Involves listening, spoken explanations, discussions, or audio-based cues.
   - Read/Write (R): Involves reading, writing, notes, or text-based materials.
3. Each question must **clearly indicate the VARK style in parentheses**, like so: (Auditory), (Read/Write), etc.
4. Ensure that **each question is self-contained and answerable using only the text provided**.
5. Number the questions sequentially (1–10) and present the answers consistently in A-B format.
6. Do **not** mix styles in a single option — each option must correspond strictly to its style if mentioned.
7. The questions **must** be "what would you most likely do" type questions to assess learning preferences.
8. Output only in the format below (no extra commentary):

EXAMPLE FORMAT:

Question 1: You need to understand how the roles in a game design team work for a project. What would you most likely do?
A. Listen to a discussion or recording about each role (Auditory)
B. Read notes or write a summary of each role (Read/Write)

Question 2: [Next question text]
A. ...
B. ...'''):
        response = llmintegration.model.generate("Generate the quiz using the provided text excerpt: "+str(RAG_SemanticSearch.results["documents"]), max_tokens=3000, n_batch=2048)
        print("Quiz Generation Response:\n", response)

    #Now with the questions, we assess the user's learning style
    VarkAssessment()
    # user_query = input("Enter your basis of query for adaptive questions: ")
        
    teaching_prompt = f"""
    You are now an adaptive educator.

    The user's learning preference is: {user_preference}.
    The user has asked for questions based on their topic: {RAG_SemanticSearch.user_query_input}.
    Using ONLY the following text excerpt:
    ---
    {str(RAG_SemanticSearch.results['documents'])}
    ---

    Generate **10 quiz questions** with 4 multiple choices formatted EXACTLY like this:

    Question 1: <question text>
    A. <choice>  
    B. <choice>  
    C. <choice>  
    D. <choice>

    REQUIREMENTS:
    - The teaching should match the user's learning style:
    - If Auditory: choices and questions should involve listening, spoken instructions, audio cues, discussion-based tasks.
    - If Read/Write: choices and questions should involve reading, writing, lists, summaries, note-taking.
    - Each option should clearly reflect the user's learning style.
    - DO NOT mention VARK, learning styles, or explain why these questions were chosen.
    - DO NOT add extra commentary.
    - Only output the questions with A to D choices.

    Begin now:
    """

    teaching_response = llmintegration.model.generate(teaching_prompt, max_tokens=3000)
    print("\n\nAdapted Teaching Output:\n")
    print(teaching_response)


        
            
except Exception as e:
    print("Error with file path:", e)