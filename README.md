# Load Balancer Project

## Overview
This project implements a customizable load balancer that distributes client requests among several server replicas using consistent hashing. The primary goal is to distribute the load evenly and efficiently among the servers using consistent hashing. The load balancer can handle server failures by spawning new replicas and ensures high availability and scalability of services.

## System Architecture

The load balancer routes client requests to server replicas, maintaining a consistent and balanced load distribution. It uses a consistent hashing mechanism with virtual servers to ensure minimal load shifts when scaling up or down.

## Coding Environment
OS: Ubuntu 20.04 LTS or above
Docker: Version 20.10.23 or above
Languages: Python 3.8 or above

### Installation
1. Install Docker
    ```bash
    sudo apt-get update
    sudo apt-get install ca-certificates curl gnupg lsb-release
    sudo mkdir -p /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update
    sudo apt-get install docker-ce docker-ce-cli containerd.io

2. Install Docker Compose
   ``` bash
   sudo curl -SL https://github.com/docker/compose/releases/download/v2.15.1/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

3. Install Python Depencies
    ```bash
   sudo apt-get install python3-pip
   pip3 install -r requirements.txt

4. Clone the repository:
    ```bash
    git clone <repo-url>
    cd load_balancer_project
    

5. Build and run the services:
   ``` bash
    make up



### Usage
- Access the load balancer at http://localhost:5000

### Testing
Run the tests using:
```bash
make test
