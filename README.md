# Load Balancer Project

## Overview
This project implements a customizable load balancer that distributes client requests among several server replicas using consistent hashing. The primary goal is distributing the load evenly and efficiently among the servers using consistent hashing. The load balancer can handle server failures by spawning new replicas and ensuring services' high availability and scalability.

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

3. Install Python Dependencies
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
2. Record the number of requests each server handles and plot a bar chart.

<p align="center">
  <img src="output1.png" alt="Experiment 1 Bar Chart">
</p>

### Observation
- The MD5 hash function resulted in an imbalanced load distribution among the servers

## Experiment 2: Scalability

1. Increment the number of server containers from 2 to 6 (launching 10,000 requests each time).
2. Plot a line chart showing the average load of the servers at each run.

<p align="center">
  <img src="task2.1.png" alt="Experiment 2 Line Chart">
</p>

### Expected Outcome
- Efficient scaling with even load distribution as server instances increase

## Experiment 3: Failure Recovery

1. Test load balancer endpoints and simulate server failures.
2. Ensure the load balancer spawns new instances to handle the load and maintain the specified number of replicas.

### Observations:
- The load balancer quickly detected the removal of 2 servers and redistributed the load.
- Response times remained stable, indicating efficient handling of server failures.
- The load balancer effectively scaled down when 2 servers were removed.
- Load distribution post-scaling was balanced, maintaining system performance.

## Experiment 4: Hash Function Modification

1. Modify the hash function: `i % 512 (number) of slots`.
2. Repeat Experiments 1 and 2, analyzing the impact on load distribution and scalability.

- Experiment 1 Results
<p align="center">
  <img src="task1.png" alt="Experiment 1 Bar Chart">
</p>
- Experiment 2 results
<p align="center">
  <img src="task4.2.png" alt="Experiment 1 Bar Chart">
</p>
