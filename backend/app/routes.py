from app import app, models
from flask import render_template, request, redirect, url_for


@app.route('/')
def index():
    return render_template('index.html')
