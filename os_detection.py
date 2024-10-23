import subprocess
import re
from colorama import Fore
import logging

# Configure logging to track OS detection results
logging.basicConfig(filename='os_detection_log.txt', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

# Validate IP address
def validate_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        print(Fore.RED + "Invalid IP address!" + Fore.WHITE)
        return False

# Run Nmap OS detection command
def detect_os(ip_address):
    print(Fore.YELLOW + f"Running OS detection on {ip_address}..." + Fore.WHITE)
    try:
        # Run the Nmap command for OS detection
        result = subprocess.run(['nmap', '-O', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Check for errors
        if result.returncode != 0:
            print(Fore.RED + f"Error running Nmap: {result.stderr.decode()}" + Fore.WHITE)
            logging.error(f"Nmap error: {result.stderr.decode()}")
            return

        # Parse and display the Nmap result
        output = result.stdout.decode()
        print(Fore.GREEN + output + Fore.WHITE)
        logging.info(f"Nmap OS Detection Result:\n{output}")

        # Extract OS information using regex (optional enhancement)
        os_match = re.search(r'OS details: (.+)', output)
        if os_match:
            detected_os = os_match.group(1)
            print(Fore.CYAN + f"Detected OS: {detected_os}" + Fore.WHITE)
        else:
            print(Fore.RED + "Unable to detect OS details." + Fore.WHITE)

    except Exception as e:
        print(Fore.RED + f"Error: {e}" + Fore.WHITE)
        logging.error(f"Exception: {e}")

if __name__ == "__main__":
    print(Fore.CYAN + "=== Nmap OS Detection ===" + Fore.WHITE)
    
    ip_address = input(Fore.YELLOW + "Enter the target IP address: " + Fore.WHITE).strip()

    # Validate IP address
    while not validate_ip(ip_address):
        ip_address = input(Fore.YELLOW + "Enter a valid IP address: " + Fore.WHITE).strip()

    detect_os(ip_address)
