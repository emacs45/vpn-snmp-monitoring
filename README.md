# VPN SNMP Monitoring Project

This project sets up a monitoring environment for a VPN server using Prometheus, Grafana, and Node Exporter.

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

3. Access the services:
    - **Prometheus UI**: [http://localhost:9090](http://localhost:9090)
    - **Node Exporter Metrics**: [http://localhost:9100/metrics](http://localhost:9100/metrics)
    - **Grafana UI**: [http://localhost:3000](http://localhost:3000) with default credentials `admin/admin`.

## Grafana Setup

1. **Add Prometheus Data Source**:
   - Go to Configuration (Gear Icon) > Data Sources > Add data source.
   - Select Prometheus.
   - Set the URL to `http://prometheus:9090`.
   - Click Save & Test.

2. **Import Node Exporter Dashboard**:
   - Click the plus icon (Create) > Import.
   - Enter `1860` in the Import via grafana.com field and click Load.
   - Select the Prometheus data source.
   - Click Import.

