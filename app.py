from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        with open('files/log', 'a') as file:
            file.write(request.data.decode())
            file.write('/')


@app.route('/clickup-comment', methods=['POST'])
def handleClickUpComment():
    if request.method == 'POST':
        return request.data


@app.route('/clickup-task')
def handleClickUpTask():
    return 'hi, clickup task'


if __name__ == '__main__':
    app.run(debug = True, port=8080)
