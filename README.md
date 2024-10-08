# VPN SNMP Monitoring

This project monitors SNMP data and stores it in an SQLite database. The collected data is served via a Flask app and can be visualized using Prometheus and Grafana.

[![CI](https://github.com/emacs45/vpn-snmp-monitoring/actions/workflows/ci.yml/badge.svg)](https://github.com/emacs45/vpn-snmp-monitoring/actions/workflows/ci.yml)
[![CD](https://github.com/emacs45/vpn-snmp-monitoring/actions/workflows/cd.yml/badge.svg?branch=main)](https://github.com/emacs45/vpn-snmp-monitoring/actions/workflows/cd.yml)

## Setup Guide

### Prerequisites

- Docker
- Docker Compose
- GitHub Personal Access Token (PAT) with the necessary permissions (`write:packages`, `read:packages`, `repo`)

#### Project Structure

```plaintext
vpn-snmp-monitoring/
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
│   │   └── cd.yml
├── scripts/
│   ├── snmp_query.py
├── webapp/
│   ├── Dockerfile
│   └── ...
├── docker-compose.yml
└── README.md
```

### Configuration

#### GitHub Secrets

Add the following secrets to your GitHub repository:

``` GHCR_PAT ``` : Your Personal Access Token for the GitHub Container Registry.

#### Docker Compose
Ensure your ``` docker-compose.yml ``` is properly configured to include services for your Flask app, Prometheus, Node Exporter, and Grafana.

#### GitHub Actions Workflows

I have set up two GitHub Actions workflows:

##### CI Workflow (.github/workflows/ci.yml)

- Checks out the code.
- Sets up Python.
- Installs dependencies.
- Runs linting and tests using flake8 and pytest.

##### CD Workflow (.github/workflows/cd.yml)

- Checks out the code.
- Sets up Docker Buildx.
- Logs in to GitHub Container Registry.
- Builds and pushes the Docker image to the registry.
- Deploys the services using Docker Compose.

## Running the Application

1. Clone the Repository:

```sh
git clone https://github.com/emacs45/vpn-snmp-monitoring.git
cd vpn-snmp-monitoring
```

2. Set Up Docker Compose:

Ensure that your docker-compose.yml is configured correctly.

Run the Application:

```sh
docker-compose up -d
```

3. Available services:
    
    - **Grafana UI**: [http://localhost:3000](http://localhost:3000) with default credentials `admin/admin`
    - **Prometheus UI**: [http://localhost:9090](http://localhost:9090)
    - **Node Exporter Metrics**: [http://localhost:9100/metrics](http://localhost:9100/metrics)
    - **SNMP Walk**: [http://localhost:5001](http://localhost:5001)

4. Additional Information

    - **Flask App**: [Flask on Github.com](https://github.com/pallets/flask) 
    - **Prometheus**: [Prometheus on Github.com](https://github.com/prometheus/prometheus)
    - **Node Exporter**: [Node Exporter on Github.com](https://github.com/prometheus/node_exporter) 
    - **Grafana**: [Grafana on Github.com](https://github.com/grafana/grafana)



For further details, refer to the individual files in the repository.

## Contributing

We welcome contributions to this project! If you are interested in contributing, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

For further details, refer to the individual files in the repository.
