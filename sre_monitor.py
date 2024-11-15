import requests
import time
import signal
import sys
import yaml


def load_config(filename):
    with open(filename, 'r') as file:
        config = yaml.safe_load(file)
       
    return config  


def initialize_counters(domains):
    counters = {}
    for domain in domains:
        domain_name = domain['url'].split('/')[2]  
        counters[domain_name] = {
            'total_requests': 0,
            'up_requests': 0
        }
    return counters


def check_endpoint(endpoint):
    method = endpoint.get('method', 'GET') 
    url = endpoint['url']
    headers = endpoint.get('headers', {})  
    body = endpoint.get('body', None) 
    
    try:
        response = requests.request(method, url, headers=headers, data=body, timeout=5)
        latency = response.elapsed.total_seconds() * 1000  # latency in ms
        is_up = (200 <= response.status_code <= 299) and (latency < 500)
    except requests.RequestException:
        is_up = False
    
  
    return is_up


def update_counters(counters, domain_name, is_up):
    counters[domain_name]['total_requests'] += 1
    if is_up:
        counters[domain_name]['up_requests'] += 1
   
   
         

def print_availability(counters):
    for domain, data in counters.items():
        if data['total_requests'] > 0:
            availability = round(100 * (data['up_requests'] / data['total_requests']))
        else:
            availability = 0
        print(f"{domain} has {availability}% availability percentage")


def handle_exit(signal, frame):
    print("\nFinal availability percentages:")
    print_availability(counters)  
    sys.exit(0)

# Main execution
if __name__ == "__main__":
    signal.signal(signal.SIGINT, handle_exit)  

    
    try:
        domains = load_config('config.yaml')  
    except FileNotFoundError:
        print("Error: config.yaml not found.")
        sys.exit(1)

    counters = initialize_counters(domains)

    
    cycle = 1
    while True:
       
        for domain in domains:
            domain_name = domain['url'].split('/')[2] 
            is_up = check_endpoint(domain)
            status = "UP" if is_up else "DOWN"
            update_counters(counters, domain_name, is_up)
     
        print_availability(counters)
        cycle += 1
        time.sleep(15)  
