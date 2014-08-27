import random
from flask import request, url_for, make_response, jsonify
from . import aim


@aim.route('/', methods=['GET', 'POST'])
def aim():
    reqData = request.data
    ddd = {'sens': random.randint(1, 99)}
    if reqData == b'yes':
        ddd['sens'] += 1000
    responseT = make_response('<h1>good Request</h1>')
    responseJ = jsonify(ddd)
    return responseJ
