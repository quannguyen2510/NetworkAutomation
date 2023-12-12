
from netmiko import ConnectHandler

f = open('ip_list.txt')
ip_list = f.read().split("\n")

all_devices = []

for ip in  ip_list:
    R = {
        "device_type" : "cisco_ios",
        "ip" : ip,
        "username" : "root",
        "password" : "quan"
    }
    all_devices.append(R)


for router in all_devices:
    net_connect = ConnectHandler(**router)
    output = net_connect.send_command("show ip int brief")

    print(output)
    print('-------')


