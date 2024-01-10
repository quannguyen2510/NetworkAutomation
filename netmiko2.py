from netmiko import ConnectHandler

def ssh_into_device(ip_address):
    # Define the device parameters
    device = {
        'device_type': 'cisco_ios',
        'ip': ip_address,
        'username': 'root',
        'password': 'quan',
    }

    try:
        # Establish an SSH connection to the device
        with ConnectHandler(**device) as ssh_conn:
            # Perform operations on the device here if needed
            print(f"Successfully connected to {ip_address}!")
            # Example: Send a command
            output = ssh_conn.send_command("show run | i hostname")
            print(output)
        ssh_conn.disconnect()
    except Exception as e:
        print(f"Error: {str(e)}")
file_paths = ['switch_ip_list.txt', 'router_ip_list.txt']
for file_path in file_paths:
    try:
        with open(file_path, 'r') as file:
            for ip_address in file:
                ip_address = ip_address.strip()  # Remove leading/trailing whitespaces
                ssh_into_device(ip_address)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error: {str(e)}")
