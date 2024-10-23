from smb.SMBConnection import SMBConnection

def smb_enum(host):
    conn = SMBConnection('', '', '', '', use_ntlm_v2=True)
    try:
        conn.connect(host, 139)
        print(f"Connected to {host}")
    except Exception as e: 
        print(f"Error: {e}")

if __name__ == "__main__":
    host = input("Enter SMB Host: ")
    smb_enum(host)
