from flask import current_app, render_template

from FAT.models import Member


@current_app.route('/')
def index():
    return render_template('index.html')