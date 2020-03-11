from flask import Flask, jsonify
import redis, os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/metric-stat')
def summary():
    r = redis.from_url(os.environ["REDIS_URL"])
    data = {
        'test': {
            'stats': {
                'valueA': int(r.hget('hpa-metric-test', 'a') or 0),
                'valueB': int(r.hget('hpa-metric-test', 'b') or 0),
            },
        },
    }
    
    return jsonify(data)

