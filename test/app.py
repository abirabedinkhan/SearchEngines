from flask import Flask
from SearchEngines.Ask import AskWeb

app = Flask(__name__)

@app.route('/')
def index():
    test = AskWeb("some stuff")
    return test.get_web_results()

if __name__ == '__main__':
    app.run(debug=True)