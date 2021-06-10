from flask import Flask, request
from app import generate_pdf

app = Flask(__name__)

@app.route("/pdf", methods=['POST', 'GET'])
def pdf():
    if request.method == 'POST':
        policyno = request.args.get('policyno')
        return str(generate_pdf(policyno))

@app.route("/")
def home():
    return "For Translate go to /pdf"

if __name__ == "__main__":
    app.run(debug = True, port = 8000)