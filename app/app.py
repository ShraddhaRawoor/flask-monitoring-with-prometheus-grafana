from flask import Flask
from prometheus_client import start_http_server, Counter, generate_latest
import random

app = Flask(__name__)

# Define a Prometheus counter metric
http_requests_total = Counter('http_requests_total', 'Total HTTP Requests')

# Homepage route
@app.route('/')
def hello():
    http_requests_total.inc()  # Increment the counter
    return "Hello from Flask!"

# Metrics route for Prometheus
@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
