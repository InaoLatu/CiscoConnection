
from netmiko import ConnectHandler
from datetime import datetime

AL = {
    'device_type': 'cisco_ios',
    'host': '10.2.187.1',
    'username': 'munics',
    'password': 'munics'
}

DL = {
    'device_type': 'cisco_ios',
    'host': '10.2.187.2',
    'username': 'munics',
    'password': 'munics'
}


FW = {
    'device_type': 'cisco_ios',
    'host': '10.2.187.3',
    'username': 'munics',
    'password': 'munics'
}


CPE = {
    'device_type': 'cisco_ios',
    'host': '10.2.187.4',
    'username': 'munics',
    'password': 'munics'
}

ISP = {
    'device_type': 'cisco_ios',
    'host': '10.2.187.5',
    'username': 'munics',
    'password': 'munics'
}

cisco_devices = [AL, DL, FW, CPE, ISP]

def main():


    for device in cisco_devices:
        net_connect = ConnectHandler(**device)
        run_conf = net_connect.send_command("sh running-config")
        hostname = net_connect.send_command("sh hostname")
        ##Get timestamp
        timestamp = datetime.now()
        print(run_conf)
        r = open(hostname+".txt", "a+")
        r.write(timestamp)
        r.write(run_conf)


if __name__ == '__main__':
    main()
