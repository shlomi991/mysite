from kubernetes import client, config
from flask import Flask
import time

app = Flask(__name__)


@app.route("/")
def hello():
    return "hello"

@app.route("/example")
def soya():
    config.load_kube_config
    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        api_response = v1.read_namespaced_pod_log(i.metadata.name, namespace='default')
        return api_response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
