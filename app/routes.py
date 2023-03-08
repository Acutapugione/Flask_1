from app import app
import time

@app.route('/')
@app.route('/index')
def index():
    return { "my_data" : "Hello, World!" }
    # return f'Current weekday is {time.strftime("%A")}'


@app.route('/qwerty', methods=['POST'])
def post():
    # return "Hello, World!"
    return "Well done"

@app.route('/qwerty', methods=['GET'])
def show_numbs():
    return f"Сума від 3 до 10: {sum(range(3, 11))}"