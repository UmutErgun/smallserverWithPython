from flask import Flask, send_file, request
import os.path
import logging
from time import strftime

api = Flask(__name__)


@api.route('/ping', methods=['GET'])
def ping():
    file_exists = os.path.exists('/tmp/ok')
    if file_exists:
        return "OK", 200
    else:
        return '', 503


@api.route('/img', methods=['GET'])
def img():
    filename = "1.png";
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    logging.info('%s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path)
    return send_file(filename, mimetype='image/gif')


if __name__ == '__main__':
    logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    api.run()
