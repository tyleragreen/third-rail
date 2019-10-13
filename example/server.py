import json
import logging

from thirdrail import ThirdRail


app = ThirdRail()


@app.route('/ping')
def get_ping():
    return json.dumps({'status': 'ok'}), '200 OK'
