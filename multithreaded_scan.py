import socket
import concurrent.futures
import logging
from queue import Queue
from colorama import Fore
import time

# Configure logging to track results
logging.basicConfig(filename='multithreaded_scan_log.txt', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

# Validate IP address
def validate_ip(ip):
    try:
        socket.inet_aton(ip)  # Quick IP validation
        return True
    except socket.error:
        print(Fore.RED + "Invalid IP address!" + Fore.WHITE)
        return False

# Port scan function
def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Set timeout to avoid hanging
            if s.connect_ex((host, port)) == 0:
                result = f"Port {port} is open on {host}"
                print(Fore.GREEN + result + Fore.WHITE)
                logging.info(result)
            else:
                logging.info(f"Port {port} is closed on {host}")
    except Exception as e:
        logging.error(f"Error scanning port {port}: {e}")

# Thread worker function
def worker(queue, host):
    while not queue.empty():
        port = queue.get()
        scan_port(host, port)
        queue.task_done()

# Multithreaded port scan controller
def multithreaded_port_scan(host, ports, num_threads=100):
    queue = Queue()

    # Populate queue with ports to scan
    for port in ports:
        queue.put(port)

    print(Fore.YELLOW + f"Starting scan on {host} with {num_threads} threads..." + Fore.WHITE)

    # Create and start threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(worker, queue, host) for _ in range(num_threads)]
        
        # Wait for all threads to finish
        concurrent.futures.wait(futures)

    print(Fore.CYAN + "Scan completed!" + Fore.WHITE)

if __name__ == "__main__":
    print(Fore.CYAN + "=== Multithreaded Port Scanner ===" + Fore.WHITE)
    
    host = input(Fore.YELLOW + "Enter the target IP address: " + Fore.WHITE).strip()

    # Validate IP before proceeding
    while not validate_ip(host):
        host = input(Fore.YELLOW + "Enter a valid IP address: " + Fore.WHITE).strip()

    # Select range of ports to scan
    try:
        start_port = int(input(Fore.YELLOW + "Enter the starting port (e.g., 1): " + Fore.WHITE))
        end_port = int(input(Fore.YELLOW + "Enter the ending port (e.g., 1024): " + Fore.WHITE))
    except ValueError:
        print(Fore.RED + "Invalid port range! Exiting." + Fore.WHITE)
        exit(1)

    # Optional: Adjust number of threads
    try:
        num_threads = int(input(Fore.YELLOW + "Enter the number of threads (default 100): " + Fore.WHITE) or 100)
    except ValueError:
        num_threads = 100

    ports_to_scan = range(start_port, end_port + 1)

    start_time = time.time()
    multithreaded_port_scan(host, ports_to_scan, num_threads=num_threads)
    end_time = time.time()

    print(Fore.GREEN + f"Scanning completed in {end_time - start_time:.2f} seconds." + Fore.WHITE)
