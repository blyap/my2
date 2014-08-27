import random
from flask import request, url_for, make_response, jsonify
from flask.ext.login import login_required, current_user
from . import aim
from .. import db
from ..models import User


@aim.route('/', methods=['GET', 'POST'])
@login_required
def aim():
    reqData = request.data
    ddd = {'sens': random.randint(1, 99)}
    ddd['size'] = current_user.aim_size
    #print(ddd['size'])
    if reqData == b'yes':
        ddd['size'] -= 0.01
    if reqData == b'miss':
        ddd['size'] += 0.01
        print('miss')
    responseT = make_response('<h1>good Request</h1>')
    current_user.aim_size = ddd['size']
    db.session.add(current_user)
    responseJ = jsonify(ddd)
    return responseJ
