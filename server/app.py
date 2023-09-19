#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    title = "Python Operations with Flask Routing and Views"
    return f"<h1>{title}</h1>"

@app.route('/print/<string>')
def print_string(string):
    print(string)
    return string

@app.route('/count/<int>')
def count(int_param):
    numbers = '\n'.join(str(i) for i in range(int_param + 1))
    return numbers

@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    num1 = float(num1)
    num2 = float(num2)
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2

    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)