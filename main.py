from flask import Flask, render_template, request
from RequestWeather import *
app = Flask(__name__, template_folder='template', static_url_path='/', static_folder='static')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error-404.html')

@app.errorhandler(500)
def page_not_found(e):
    return render_template('error-500.html')

@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    return render_template('WeatherSearch.html')

@app.route('/search', methods=['POST'])
def search():
    name = request.form['name']
    result = GetWeather(name)
    if len(result) == 0:
        return render_template('NotFind.html')
    else:
        return render_template('Weather.html', weather=result[0], info=result[1])


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1')