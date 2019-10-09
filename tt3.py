
from netmiko import ConnectHandler

AL = {
    'device_type': 'cisco_ios',
    'host': '10.2.187.1',
    'username': 'munics',
    'password': 'munics'
}

def main():
    al_connect = ConnectHandler(**AL)
    al_connect.find_prompt()
    al_run_conf = al_connect.send_command("sh running-config")
    print(al_run_conf)

    pass

if __name__ == '__main__':
    main()
