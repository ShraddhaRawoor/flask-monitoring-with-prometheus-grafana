# Flask Monitoring with Prometheus and Grafana

This project demonstrates how to monitor a Flask web application using:
- **Prometheus** for scraping metrics
- **Grafana** for visualizing data
- **Alertmanager** for triggering alerts

## Features

- Live metrics from Flask via `/metrics`
- Dockerized setup
- Alerts when Flask app goes down
- Beautiful Grafana dashboards

## Setup Instructions

Run the following command to start all services:

```bash
docker-compose up --build

