from netmiko import ConnectHandler

def ssh_into_device(ip_address, username, password, device_type='cisco_ios'):
    # Define the device parameters
    device = {
        'device_type': device_type,
        'ip': ip_address,
        'username': username,
        'password': password,
    }

    try:
        # Establish an SSH connection to the device
        with ConnectHandler(**device) as ssh_conn:
            # Perform operations on the device here if needed
            print(f"Successfully connected to {ip_address}!")
            # Example: Send a command
            output = ssh_conn.send_command("show version")
            print("Output of 'show version':")
            print(output)

    except Exception as e:
        print(f"Error: {str(e)}")

# Replace 'your_username' and 'your_password' with the actual credentials
with open('switch_ip_list.txt', 'r') as file:
    for ip_address in file:
        ip_address = ip_address.strip()  # Remove leading/trailing whitespaces
        ssh_into_device(ip_address, "your_username", "your_password")
