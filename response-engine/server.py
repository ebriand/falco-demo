#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import json
from kubernetes import client, config

config.load_incluster_config()
v1 = client.CoreV1Api()

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        data = json.loads(post_data)
        logging.info("%s\n", data["output"])
        if (data["priority"] != "Notice" and data["priority"] != "Informational" and data["priority"] != "Debug"):
           namespace = data["output_fields"]["k8s.ns.name"]
           pod = data["output_fields"]["k8s.pod.name"]
           logging.info("Deleting pod %s in namespace %s", pod, namespace)
           v1.delete_namespaced_pod(pod, namespace)
           logging.info("Pod %s deleted", pod)
        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
