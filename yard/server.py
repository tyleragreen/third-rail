import json
import logging

from thirdrail import ThirdRail


app = ThirdRail()


@app.consist('/ping')
def get_ping():
    return json.dumps({'status': 'ok'}), '200 OK'


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)-8s %(message)s')
    app.start(port=5050)
