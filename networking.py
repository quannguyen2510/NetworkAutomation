from netmiko import ConnectHandler

f = open('switch_ip_list.txt')
ip_list = f.read().split("\n")

all_devices = []

for ip in ip_list:
    R = {
        "device_type": "cisco_ios",
        "ip": ip,
        "username": "root",
        "password": "quan",
        "port": 23
    }
    all_devices.append(R)

for switch in all_devices:
    try:
        net_connect = ConnectHandler(**switch)
        output = net_connect.send_command("show run | i hostname")

        print(output)
        print('-------')

        net_connect.disconnect()  # Disconnect after each successful connection
    except Exception as e:
        print(f"Failed to connect to {switch['ip']} with error: {str(e)}")
