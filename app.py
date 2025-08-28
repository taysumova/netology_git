from flask import Flask

app = Flask(__name__)

a = 18
b = 6

@app.route("/")
def home():
    res = "<h1>Hello from Python!</h1>\n"
    res += f'<p>{a} / {b} = {(divide(a, b))}</p>\n'
    res += f'<p>{a} * {b} = {(multiply(a, b))}</p>\n'
    return res

def divide (a, b):
    return a // b

def multiply (a, b):
    return a * b


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)