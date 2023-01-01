from kubernetes import client, config
from flask import Flask
import time

app = Flask(__name__)

# def main():
#     return ("Client core shit")
#     config.load_kube_config()
    
#     v1 = client.CoreV1Api()
#     print("Listing pods with their IPs:")
#     ret = v1.list_pod_for_all_namespaces(watch=False)
#     for i in ret.items:
#         print("%s\t%s\t%s" %
#               (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

@app.route("/")
def hello():
    return "Don hamelech!"

@app.route("/example")
def soya():
    # return ("Client core shit")
    config.load_kube_config
    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        api_response = v1.read_namespaced_pod_log(i.metadata.name, namespace='default')
        print(api_response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)



# from kubernetes import client, config, watch
# from flask import Flask

# app = Flask(__name__)


# # Configs can be set in Configuration class directly or using helper utility
# def json():
#     config.load_incluster_config()
#     v1 = client.CoreV1Api()
#     print("Listing pods with their IPs:")
#     ret = v1.list_pod_for_all_namespaces(watch=False)
#     for i in ret.items:
#         print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

# # pod_name = "counter"
# # # def json():
# # #     api_instance = client.CoreV1Api()
# # #     pod_name = api_instance.list_namespaced_pod(namespace, label_selector="app=" +"mysite-nginx")
# # #     api_response = api_instance.read_namespaced_pod(name=pod_name, namespace='default')
# # #     print(api_response)

# @app.route("/")
# def hello():
#     return "change, World!"



# if __name__ == '__main__':
#     # Run the app server on localhost:5000
#     app.run(host='0.0.0.0', port=5000, debug=False)



