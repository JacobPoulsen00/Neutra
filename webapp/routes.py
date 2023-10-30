from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "some_secret_key"  # Needed for flash messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
