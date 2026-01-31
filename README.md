# RealtimeSalesStreaming
Real-Time Sales Monitoring Dashboard

## Installation

pip install -r requirements.txt

## Run with Docker

docker build -t realtime-sales .
docker run -p 8501:8501 realtime-sales

## Tech Stack
- Python
- Streamlit
- Redis Streams
- Docker

## Architecture
Producer → Redis Streams → Consumer → Streamlit Dashboard

## Use Cases
- Real-time analytics
- Monitoring sales spikes
- Data streaming projects
