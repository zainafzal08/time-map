from flask import Flask
import os
import base64

app = Flask(__name__)
app.secret_key = base64.b64encode(os.urandom(24)).decode("utf-8")

@app.route('/api/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True)
