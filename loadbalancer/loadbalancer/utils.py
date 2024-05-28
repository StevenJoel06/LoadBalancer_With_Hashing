import os

def create_server(hostname=None):
    command = f"docker run -d --network load_balancer_project_default"
    if hostname:
        command += f" --name {hostname}"
    command += " server_image"
    os.system(command)

def remove_server(hostname):
    if hostname:
        os.system(f"docker stop {hostname} && docker rm {hostname}")