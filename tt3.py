
from netmiko import ConnectHandler
from datetime import datetime

AL = {
    'device_type': 'cisco_ios',
    'host': '10.2.187.1',
    'username': 'munics',
    'password': 'munics',
    'name': 'AL'
}

DL = {
    'device_type': 'cisco_ios',
    'host': '10.2.187.2',
    'username': 'munics',
    'password': 'munics',
    'name': 'DL'
}


FW = {
    'device_type': 'cisco_ios',
    'host': '10.2.187.3',
    'username': 'munics',
    'password': 'munics',
    'name': 'FW'
}


CPE = {
    'device_type': 'cisco_ios',
    'host': '10.2.187.4',
    'username': 'munics',
    'password': 'munics',
    'name': 'CPE'
}

ISP = {
    'device_type': 'cisco_ios',
    'host': '10.2.187.5',
    'username': 'munics',
    'password': 'munics',
    'name': 'ISP'
}

cisco_devices = [AL, DL, FW, CPE, ISP]

def main():


    for device in cisco_devices:
        net_connect = ConnectHandler(**device)
        run_conf = net_connect.send_command("sh running-config")
        hostname = device.get('name')
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(run_conf)
        r = open(hostname+timestamp+".txt", "a+")
        r.write(timestamp)
        r.write(run_conf)


if __name__ == '__main__':
    main()
