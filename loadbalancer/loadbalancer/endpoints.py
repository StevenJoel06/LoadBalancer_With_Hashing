from flask import Blueprint, request, jsonify
import requests
from consistent_hash import ConsistentHash
from utils import create_server, remove_server
import os

# Create a Blueprint for the load balancer endpoints
lb_blueprint = Blueprint('lb', __name__)

# Parameters
N = int(os.getenv("NUM_SERVERS", 3))
M = 512  # Number of slots
K = 9    # Number of virtual servers
hash_ring = ConsistentHash(M, K, N)

@lb_blueprint.route('/rep', methods=['GET'])
def get_replicas():
    return jsonify({"message": {"N": hash_ring.num_servers, "replicas": hash_ring.get_servers()}, "status": "successful"}), 200

@lb_blueprint.route('/add', methods=['POST'])
def add_server():
    data = request.get_json()
    n = data.get('n')
    hostnames = data.get('hostnames', [])
    if len(hostnames) > n:
        return jsonify({"message": "<Error> Length of hostname list is more than newly added instances", "status": "failure"}), 400
    
    for i in range(n):
        hostname = hostnames[i] if i < len(hostnames) else None
        create_server(hostname)
    hash_ring.add_servers(n)
    return jsonify({"message": {"N": hash_ring.num_servers, "replicas": hash_ring.get_servers()}, "status": "successful"}), 200

@lb_blueprint.route('/rm', methods=['DELETE'])
def remove_server():
    data = request.get_json()
    n = data.get('n')
    hostnames = data.get('hostnames', [])
    if len(hostnames) > n:
        return jsonify({"message": "<Error> Length of hostname list is more than removable instances", "status": "failure"}), 400
    
    for i in range(n):
        hostname = hostnames[i] if i < len(hostnames) else None
        remove_server(hostname)
    hash_ring.remove_servers(n)
    return jsonify({"message": {"N": hash_ring.num_servers, "replicas": hash_ring.get_servers()}, "status": "successful"}), 200

@lb_blueprint.route('/<path:path>', methods=['GET'])
def route_request(path):
    server = hash_ring.get_server(path)
    response = requests.get(f'http://{server}:5000/{path}')
    return response.json(), response.status_code
