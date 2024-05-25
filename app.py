
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        subject = request.form['subject']
        quiz_subject = analyze_subject(subject)
        return render_template('quiz.html', subject=quiz_subject)
    return render_template('index.html')

def analyze_subject(subject):
    # Simple keyword matching for demonstration
    if 'math' in subject.lower():
        return 'Mathematics'
    elif 'science' in subject.lower():
        return 'Science'
    elif 'history' in subject.lower():
        return 'History'
    else:
        return 'General Knowledge'

if __name__ == "__main__":
    app.run(debug=True)
