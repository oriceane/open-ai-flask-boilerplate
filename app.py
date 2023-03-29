from flask import Flask, render_template, request, redirect, url_for, flash
import config

app = Flask(__name__, static_folder=config.UPLOAD_FOLDER)

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())


@app.route('/some-page', methods=["GET", "POST"])
def somePage():
    return render_template('some-page.html', **locals())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
