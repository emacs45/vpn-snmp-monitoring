# VPN SNMP Monitoring

This project monitors SNMP data and stores it in an SQLite database. The collected data is served via a Flask app and can be visualized using Prometheus and Grafana.

## Setup Guide

### Prerequisites

- Docker
- Docker Compose
- GitHub Personal Access Token (PAT) with the necessary permissions (`write:packages`, `read:packages`, `repo`)

### Project Structure

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

### GitHub Secrets

Add the following secrets to your GitHub repository:

``` GHCR_PAT ``` : Your Personal Access Token for the GitHub Container Registry.

### Docker Compose
Ensure your ``` docker-compose.yml ``` is properly configured to include services for your Flask app, Prometheus, Node Exporter, and Grafana.

### GitHub Actions Workflows

I have set up two GitHub Actions workflows:

### CI Workflow (.github/workflows/ci.yml)

- Checks out the code.
- Sets up Python.
- Installs dependencies.
- Runs linting and tests using flake8 and pytest.

### CD Workflow (.github/workflows/cd.yml)

- Checks out the code.
- Sets up Docker Buildx.
- Logs in to GitHub Container Registry.
- Builds and pushes the Docker image to the registry.
- Deploys the services using Docker Compose.

### Running the Application

1. Clone the Repository:

```sh
git clone https://github.com/your_github_username/vpn-snmp-monitoring.git
```
```sh
cd vpn-snmp-monitoring
```

2. Set Up Docker Compose:

Ensure that your docker-compose.yml is configured correctly.

Run the Application:

```sh
docker-compose up -d
```

3. Access the services:
    
    - **Prometheus UI**: [http://localhost:9090](http://localhost:9090)
    - **Node Exporter Metrics**: [http://localhost:9100/metrics](http://localhost:9100/metrics)
    - **Grafana UI**: [http://localhost:3000](http://localhost:3000) with default credentials `admin/admin`.

### Additional Information

**Flask App**: Serves SNMP data and can be accessed on port 5000
**Prometheus**: Collects metrics and can be accessed on port 9090
**Node Exporter**: Exposes hardware and OS metrics and can be  accessed on port 9100
**Grafana**: Visualizes metrics and can be accessed on port 3000

For further details, refer to the individual files in the repository.
