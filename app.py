from flask import Flask, render_template, request
import PyPDF2
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['resume']
    job_desc = request.form['job_desc']

    if file:
        pdf_reader = PyPDF2.PdfReader(file)
        resume_text = ""

        for page in pdf_reader.pages:
            resume_text += page.extract_text()

        # lowercase
        resume_text = resume_text.lower()
        job_desc = job_desc.lower()

        # remove punctuation
        resume_text = re.sub(r'[^\w\s]', '', resume_text)
        job_desc = re.sub(r'[^\w\s]', '', job_desc)

        # 🔥 IMPORTANT SKILLS LIST
        important_skills = [
            "python", "sql", "machine learning", "data analysis",
            "tensorflow", "aws", "cloud", "communication",
            "problem solving"
        ]

        matched = []
        missing = []

        for skill in important_skills:
            if skill in job_desc:
                if skill in resume_text:
                    matched.append(skill)
                else:
                    missing.append(skill)

        # score
        if len(matched) + len(missing) > 0:
            score = int((len(matched) / (len(matched) + len(missing))) * 100)
        else:
            score = 0

        return render_template("result.html", score=score, matched=matched, missing=missing)

    return "Error"


if __name__ == '__main__':
    app.run(debug=True)