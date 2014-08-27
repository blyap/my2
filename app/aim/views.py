import random
from flask import request, url_for, make_response, jsonify
from . import aim


@aim.route('/', methods=['GET', 'POST'])
def aim():
    reqData = request.data
    if reqData == b'start':
        print(reqData)
    responseT = make_response('<h1>good Request</h1>')
    ddd = {'sens': random.randint(1, 99)}
    responseJ = jsonify(ddd)
    return responseJ
