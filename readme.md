# SRE Monitoring Script

A Python-based monitoring tool that tracks the availability and performance of multiple endpoints, providing real-time statistics on uptime and response times.

## Features

- Monitors multiple endpoints configured via a YAML file
- Supports various HTTP methods (`GET`, `POST`, etc.)
- Validates response latency (with a threshold of < 500ms)
- Checks for successful HTTP responses (status codes in the 2xx range)
- Logs availability percentages for each domain
- Provides real-time monitoring feedback in the console
- Gracefully handles program termination with detailed final statistics

## Requirements

- Python 3.x
- `requests` module for making HTTP requests 
- `pyyaml` module for parsing YAML configuration files

## Installation

1. **Clone the repository**

2. **Set up a virtual environment**:
   ```bash
   # Create a virtual environment (Python 3)
   python3 -m venv venv
   
   # Create a virtual environment (Python 2) 
   python -m venv venv

   # Activate the environment (Windows)
   .\venv\Scripts\activate

   # Activate the environment (macOS/Linux)
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   # Using the provided requirements file
   pip install -r requirements.txt
   ```

## Configuration

Create a `config.yaml` file to specify the endpoints to monitor. Example:

```yaml
- method: GET
  name: Fetch Index Page
  url: https://fetch.com/

- method: GET 
  name: Fetch Careers Page
  url: https://fetch.com/careers

- body: '{"foo": "bar"}'
  method: POST
  name: Fetch Fake Post Endpoint
  url: https://fetch.com/some/post/endpoint

- name: Fetch Rewards Index Page
  url: https://www.fetchrewards.com/
```

### Key Fields in Configuration:

- `method`: (Optional) HTTP method (`GET`, `POST`, etc.). Defaults to `GET` if omitted.
- `name`: (Required) A descriptive name for the endpoint.
- `url`: (Required) The URL of the endpoint.
- `headers`: (Optional) HTTP headers as key-value pairs.
- `body`: (Optional) JSON-encoded string for the HTTP request body (used for `POST`, etc.).

## Usage

Run the script by providing the path to your `config.yaml` file:

```bash
# Python 3
python3 sre_monitor.py path/to/config.yaml

# Python 2
python sre_monitor.py path/to/config.yaml
```

The script will monitor endpoints, log availability, and display results.

## How It Works

### Monitoring Workflow

1. Reads `config.yaml` to configure endpoints.
2. Sends HTTP requests to each endpoint every 15 seconds.
3. Evaluates responses based on status code and latency.
4. Logs availability percentages for each domain.


