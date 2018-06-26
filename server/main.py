from flask import Flask
import os
import base64

app = Flask(__name__)
app.secret_key = base64.b64encode(os.urandom(24)).decode("utf-8")

def json_response(j):
    response = app.response_class(
        response = json.dumps(j),
        status = 200,
        mimetype = 'application/json'
    )
    return response

def get_user():
    u = User("test")
    g = Group("test_group",[])
    u.groups = []
    return

@app.route('/api/user')
def hello_world():
    u = get_user()
    return json_response(u.to_dict())

if __name__ == "__main__":
    app.run(debug=True)
