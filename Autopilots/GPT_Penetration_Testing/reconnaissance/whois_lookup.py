import whois

def whois_lookup(domain):
    try:
        info = whois.whois(domain)
        print(info)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    domain = input("Enter domain: ")
    whois_lookup(domain)
