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
   # Create a virtual environment
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

   # Alternatively, install dependencies manually
   pip install requests pyyaml
   ```

## Configuration

Create a `config.yaml` file to specify the endpoints to monitor. Below is an example:

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

- `method`: (Optional) HTTP method (`GET`, `POST`, etc.). Defaults to `GET` if omitted
- `name`: (Required) A descriptive name for the endpoint
- `url`: (Required) The URL of the endpoint
- `headers`: (Optional) HTTP headers as key-value pairs
- `body`: (Optional) JSON-encoded string for the HTTP request body (used for `POST`, etc.)

## Usage

Run the script by providing the path to your `config.yaml` file as an argument:

```bash
python sre_monitor.py path/to/config.yaml
```

The script will:
- Continuously monitor all endpoints every 15 seconds
- Log availability percentages for each domain
- Display detailed results for each test cycle

### Example Console Output

```text
Test cycle #1 begins:
Endpoint Fetch Index Page (https://fetch.com/) => UP
Endpoint Fetch Careers Page (https://fetch.com/careers) => DOWN
Endpoint Fetch Fake Post Endpoint (https://fetch.com/some/post/endpoint) => DOWN
Endpoint Fetch Rewards Index Page (https://www.fetchrewards.com/) => UP

fetch.com has 33% availability percentage
www.fetchrewards.com has 100% availability percentage
```

Press `Ctrl+C` to terminate the program.
## How It Works

### Monitoring Workflow

1. The script reads the `config.yaml` file to configure endpoints
2. It sends HTTP requests to each endpoint every 15 seconds
3. It evaluates responses based on:
   - Status code in the 2xx range
   - Response latency less than 500ms
4. Availability percentages for each domain are logged after every test cycle

### Key Components

- **Endpoint Checker**: Sends HTTP requests and validates responses
- **Domain Availability Tracker**: Tracks and calculates uptime percentages
- **Graceful Exit Handler**: Outputs final availability statistics upon user termination

## Troubleshooting

- **FileNotFoundError**: Ensure the correct path to `config.yaml` is provided when running the script
- **ImportError**: Verify that all required dependencies are installed using `pip install -r requirements.txt`
- **Invalid Configurations**: Ensure the YAML file is properly formatted and adheres to the schema

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.