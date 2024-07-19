from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from docx import Document
import openai, os
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from starlette.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI()

# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:63342",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# OpenAI API key setup
openai.api_key = os.environ['OPENAI_API_KEY']

# Document path
doc_path = 'Python Exercise.docx'

# Extract text from Word document
def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)


# Function to ask a question about the text
def ask_question_about_text(chain, document_text, question):
    inputs = {'document_text': document_text, 'question': question}
    response = chain.run(inputs)
    return response


# Define the prompt template
template = PromptTemplate.from_template("Here is a document:\n\n{document_text}\n\nQuestion: {question}\nAnswer:")

# Initialize LangChain with OpenAI
llm = OpenAI(api_key=openai.api_key)
chain = LLMChain(prompt=template, llm=llm)

# Get document text
document_text = extract_text_from_docx(doc_path)


def get_question(question: str):
    # Get the answer to the question
    answer = ask_question_about_text(chain, document_text, question)
    return answer


# FastAPI endpoint to handle POST requests
@app.post("/ask-question/")
async def ask_question(question: str = Form(...)):
    # Get the answer to the question
    answer = get_question(question)

    # Return the answer as a JSON response
    return JSONResponse(content={"answer": answer})


# Run the FastAPI app using Uvicorn
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
