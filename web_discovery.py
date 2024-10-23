import subprocess
import logging
from colorama import Fore

# Configure logging to track results
logging.basicConfig(filename='web_exploit_discovery_log.txt', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

def run_sqlmap(url):
    print(Fore.YELLOW + f"Running SQLMap on {url}..." + Fore.WHITE)
    try:
        # Running SQLMap to test for SQL injection vulnerabilities
        result = subprocess.run(['sqlmap', '-u', url, '--batch', '--risk=3', '--level=5'], 
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Check for errors
        if result.returncode != 0:
            print(Fore.RED + f"Error running SQLMap: {result.stderr.decode()}" + Fore.WHITE)
            logging.error(f"SQLMap error: {result.stderr.decode()}")
            return

        # Display the output
        output = result.stdout.decode()
        print(Fore.GREEN + output + Fore.WHITE)
        logging.info(f"SQLMap Output:\n{output}")

    except Exception as e:
        print(Fore.RED + f"Exception: {e}" + Fore.WHITE)
        logging.error(f"Exception: {e}")

def run_gobuster(url):
    print(Fore.YELLOW + f"Running Gobuster on {url}..." + Fore.WHITE)
    try:
        # Running Gobuster to discover directories/files
        # You need to specify a path to a wordlist; here using a sample one
        wordlist = '/usr/share/wordlists/dirb/common.txt'  # Change to your wordlist path
        result = subprocess.run(['gobuster', 'dir', '-u', url, '-w', wordlist, '-t', '50'],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Check for errors
        if result.returncode != 0:
            print(Fore.RED + f"Error running Gobuster: {result.stderr.decode()}" + Fore.WHITE)
            logging.error(f"Gobuster error: {result.stderr.decode()}")
            return

        # Display the output
        output = result.stdout.decode()
        print(Fore.GREEN + output + Fore.WHITE)
        logging.info(f"Gobuster Output:\n{output}")

    except Exception as e:
        print(Fore.RED + f"Exception: {e}" + Fore.WHITE)
        logging.error(f"Exception: {e}")

if __name__ == "__main__":
    print(Fore.CYAN + "=== Web Exploit Discovery ===" + Fore.WHITE)

    url = input(Fore.YELLOW + "Enter the target URL (e.g., http://example.com): " + Fore.WHITE).strip()

    print(Fore.CYAN + "Choose a tool to run:" + Fore.WHITE)
    print("1. SQLMap")
    print("2. Gobuster")

    choice = input(Fore.YELLOW + "Enter your choice (1/2): " + Fore.WHITE).strip()

    if choice == '1':
        run_sqlmap(url)
    elif choice == '2':
        run_gobuster(url)
    else:
        print(Fore.RED + "Invalid choice! Exiting." + Fore.WHITE)
