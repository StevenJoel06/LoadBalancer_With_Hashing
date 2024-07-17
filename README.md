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
```
# Performance Analysis

## Experiment 1: Load Distribution

1. Launch 10,000 asynchronous requests on 3 server containers.
2. Record the number of requests handled by each server and plot a bar chart.

![Experiment 1 Bar Chart](images/experiment1.png)

### Expected Outcome
- Even distribution of load among server instances

## Experiment 2: Scalability

1. Increment the number of server containers from 2 to 6 (launching 10,000 requests each time).
2. Plot a line chart showing the average load of the servers at each run.

![Experiment 2 Line Chart](images/experiment2.png)

### Expected Outcome
- Efficient scaling with even load distribution as server instances increase.

## Experiment 3: Failure Recovery

1. Test load balancer endpoints and simulate server failures.
2. Ensure the load balancer spawns new instances to handle the load and maintain the specified number of replicas.

![Experiment 3 Image](images/experiment3.png)

## Experiment 4: Hash Function Modification

1. Modify the hash function: `i % 512 (number) of slots`.
2. Repeat Experiments 1 and 2, analyzing the impact on load distribution and scalability.

- Experiment 1
![Experiment 4 Image](images/experiment4.png)

- Experiment 2
![Experiment 4 Image](images/experiment4.png)
