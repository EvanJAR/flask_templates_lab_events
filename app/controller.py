from flask import render_template
from app import app
from app.models.events_list import events

@app.route('/')
def index():
    return render_template('index.html', title='Home', events=events)