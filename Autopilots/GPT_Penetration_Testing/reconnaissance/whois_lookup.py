import whois
import re

def is_valid_domain(domain):
    """Validate the domain name using a regex pattern."""
    pattern = re.compile(
        r'^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'
    )
    return pattern.match(domain) is not None

def whois_lookup(domain):
    """Perform a WHOIS lookup and print the result."""
    try:
        info = whois.whois(domain)
        
        # Extract some key data if available
        print(f"\nWHOIS Data for {domain}:")
        print(f"Domain Name: {info.domain_name}")
        print(f"Registrar: {info.registrar}")
        print(f"Creation Date: {info.creation_date}")
        print(f"Expiration Date: {info.expiration_date}")
        print(f"Name Servers: {', '.join(info.name_servers or [])}\n")

        return info

    except whois.parser.PywhoisError:
        print(f"WHOIS lookup failed: Domain '{domain}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def save_to_file(data, filename="whois_result.txt"):
    """Save WHOIS data to a text file."""
    try:
        with open(filename, 'w') as f:
            f.write(str(data))
        print(f"WHOIS result saved to {filename}")
    except Exception as e:
        print(f"Failed to save the file: {e}")

if __name__ == "__main__":
    domain = input("Enter domain: ").strip().lower()

    if is_valid_domain(domain):
        result = whois_lookup(domain)
        if result:
            save_option = input("Do you want to save the result to a file? (y/n): ").strip().lower()
            if save_option == 'y':
                save_to_file(result)
    else:
        print("Invalid domain format. Please enter a valid domain.")
