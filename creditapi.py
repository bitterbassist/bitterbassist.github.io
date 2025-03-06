from flask import Flask, jsonify
from gevent.pywsgi import WSGIServer
import json
import random
import logging
import sys

app = Flask(__name__)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter('%(levelname)s:%(message)s'))
logger.addHandler(handler)

def random_bool():
    return random.choice([True, False])

def is_script_running():
    # Always returns True to indicate that the script is active
    return True

if __name__ == '__main__':
    print("Script is running:", is_script_running())
    # Optionally, you can also test the random_bool function
    print("Random boolean value:", random_bool())

@app.route('/Users\Revenant\credits')
def credits():
    try:
        with open("credits_log.json", "r") as file:
            credits_data = json.load(file)
        # Log that the file was successfully read
        logging.info("Successfully read from credits_log.json")
    except Exception as e:
        credits_data = {"error": str(e)}
        # Log the error
        logging.error("Failed to read from credits_log.json: %s", e)
    return jsonify(credits_data)

if __name__ == '__main__':
    # Debug/Development
    # app.run(debug=True, host="0.0.0.0", port="5000")
    # Production
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
