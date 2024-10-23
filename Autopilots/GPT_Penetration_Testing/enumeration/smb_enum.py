from smb.SMBConnection import SMBConnection
import socket

def smb_enum(host, username='', password='', port=139):
    """Attempt to connect to an SMB host and enumerate shares."""
    conn = SMBConnection(username, password, '', '', use_ntlm_v2=True)
    
    try:
        # Attempt to connect to the SMB service
        print(f"Connecting to {host} on port {port}...")
        conn.connect(host, port, timeout=5)
        print(f"Connected to {host} on port {port}!")

        # Try to enumerate shares
        shares = conn.listShares()
        if shares:
            print("Available Shares:")
            for share in shares:
                print(f" - {share.name} (Description: {share.comments})")
        else:
            print("No shares found or enumeration failed.")
    
    except socket.timeout:
        print(f"Connection to {host}:{port} timed out.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    host = input("Enter SMB Host: ").strip()
    port = input("Enter SMB Port (139 or 445) [default: 139]: ").strip() or '139'
    
    # Convert port to integer and validate it
    if port not in {'139', '445'}:
        print("Invalid port. Please enter 139 or 445.")
    else:
        username = input("Enter Username (optional): ").strip()
        password = input("Enter Password (optional): ").strip()
        
        smb_enum(host, username, password, int(port))
