from flask import Flask, make_response, render_template, request
import my_mongo
import json
app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    args = request.args
    f = open("args.json", "w")
    args_str = json.dumps(args, indent = 2)
    print(args_str)
    f.write(args_str)
    f.close()
    return 'my_mongo.mongo_test()'


@app.route("/api/auth/user", methods=['GET'])
def user():
    return 'my_mongo.mongo_test()'


@app.route('/api/auth/login', methods=['POST', 'GET'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    found = my_mongo.get_record('users', {'email': email})
    print(found)
    resp = make_response('OK')
    resp.set_cookie('userID', 'coookzzzz')
    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
