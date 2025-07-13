import docx
import PyPDF2

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        return "\n".join([page.extract_text() for page in reader.pages])
job_description = """
We are looking for a Python Developer with experience in machine learning, data analysis, and web development.
Skills required: Python, Scikit-learn, Pandas, Flask, REST APIs, SQL, Git.
"""

required_skills = ["python", "scikit-learn", "pandas", "flask", "rest apis", "sql", "git"]
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

def analyze_resume(text, skills):
    tokens = word_tokenize(text.lower())
    matched_skills = [skill for skill in skills if skill in tokens]
    score = len(matched_skills) / len(skills) * 100
    return matched_skills, score
def run_analyzer(file_path, file_type='pdf'):
    if file_type == 'pdf':
        resume_text = extract_text_from_pdf(file_path)
    else:
        resume_text = extract_text_from_docx(file_path)

    matched_skills, score = analyze_resume(resume_text, required_skills)
    print(f"Matched Skills: {matched_skills}")
    print(f"Resume Score: {score:.2f}%")
