from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello Corrientes!'

if __name__ == '__main__':
    # This block is ignored by Zappa/AWS Lambda, but allows local development
    app.run(debug=True)
