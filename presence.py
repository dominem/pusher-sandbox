import json
import uuid

import pusher

from flask import Flask, request, make_response

import secrets


pusher_client = pusher.Pusher(
    app_id=secrets.APP_ID,
    key=secrets.KEY,
    secret=secrets.SECRET,
    cluster=secrets.CLUSTER,
    ssl=secrets.SSL
)


app = Flask(__name__)


@app.route('/pusher/auth', methods=['GET'])
def pusher_auth():
    socket_id = request.args['socket_id']
    channel = request.args['channel_name']
    presence_data = {'user_id': str(uuid.uuid4())}
    auth = pusher_client.authenticate(
        channel=channel,
        socket_id=socket_id,
        custom_data=presence_data
    )
    callback = request.args['callback']
    callback += f'({auth})'
    resp = make_response(callback)
    resp.mimetype = 'application/javascript'
    return resp
