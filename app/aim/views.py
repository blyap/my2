from flask import render_template, request, url_for, make_response, jsonify
from . import aim


@aim.route('/', methods=['GET', 'POST'])
def aim():
    reqData = request.data
    if reqData == b'start':
        print(reqData)
    responseT = make_response('<h1>good Request</h1>')
    responseJ = jsonify({'ttt': 111})
    return responseJ
