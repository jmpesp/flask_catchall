#!/usr/bin/env python

import time
import json


from flask import Flask, request, jsonify, request, Response
app = Flask(__name__)


# http://flask.pocoo.org/snippets/57/
@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    headers = {}
    for key,value in request.headers:
        headers[key] = value
    response = {
        "path": path,
        "headers": headers,
        "args": request.args,
        "form": request.form,
        "raw_data": request.data,
    }
    response = json.dumps(response, indent=2, default=str)

    if path == "sleep":
        time.sleep(int(request.args["time"]))

    print(response)
    resp = Response(response)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == "__main__":
    #app.debug = True
    app.run(host="0.0.0.0", port=12345)

