from flask import current_app, render_template


@current_app.route('/')
def index():
    return render_template('index.html')