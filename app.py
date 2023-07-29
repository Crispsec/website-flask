from flask import Flask, render_template
import json

app = Flask(__name__)

# resume_data = json.load(open('resume.json')) 

@app.route('/')
def home():
    with open('resume.json') as json_file:
        resume_data = json.load(json_file)
    return render_template('index.html', data=resume_data)

if __name__ == '__main__':
    app.run()