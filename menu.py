from flask import Flask, url_for, render_template, make_response, jsonify, request
from data import db_session

app = Flask(__name__)


@app.errorhandler(404)
def not_found(_):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/')
@app.route('/home')
def index():
    return render_template('main.html')


@app.route('/abo-oops')
def about_films_but_oops():
    return render_template('about_films.html')


@app.route('/registered')
def registered():
    return render_template('registered.html')


@app.route('/sign-up')
def sign_up():
    return render_template('sign-up.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')