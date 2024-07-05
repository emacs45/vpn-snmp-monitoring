# VPN SNMP Monitoring Project

This project sets up a monitoring environment for a VPN server using Prometheus, Grafana, and SNMP Exporter. It also includes a Python script for SNMP queries.

## Prerequisites

- Docker
- Docker Compose

## Setup

1. Clone the repository:

    ```sh
    git clone https://github.com/emacs45/vpn-snmp-monitoring.git
    cd vpn-snmp-monitoring
    ```

2. Start the services:

    ```sh
    docker-compose up -d
    ```

3. Access Grafana at [http://localhost:3000](http://localhost:3000) with default credentials `admin/admin`.

## Python Script

The `snmp_query.py` script can be used to query SNMP data.

```sh
python scripts/snmp_query.py
