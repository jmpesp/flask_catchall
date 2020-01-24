#!/usr/bin/env python

import time
import json


from flask import Flask, request, jsonify, request
app = Flask(__name__)


# http://flask.pocoo.org/snippets/57/
@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    headers = {}
    for key,value in request.headers:
        headers[key] = value
    response = {"path": path, "headers": headers, "args": request.args}
    response = json.dumps(response, indent=2)
    print(response)
    return response


if __name__ == "__main__":
    #app.run(host="0.0.0.0", debug=True, port=12345)
    app.run(host="0.0.0.0", port=12345)

