# Load Balancer Project

## Overview
This project implements a customizable load balancer that distributes client requests among several server replicas using consistent hashing.

## Setup

### Prerequisites
- Docker 20.10.23 or above
- Docker Compose 2.15.1 or above
- Make

### Installation
1. Clone the repository:
    bash
    git clone <repo-url>
    cd load_balancer_project
    

2. Build and run the services:
    bash
    make up
    

### Usage
- Access the load balancer at http://localhost:5000

### Testing
Run the tests using:
```bash
make test