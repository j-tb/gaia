# Install the Python Requests library:
# `pip install requests`

import requests
import json


netbox_url = "docker-01"
netbox_port = "32775"
netbox_token = "0123456789abcdef0123456789abcdef01234567"
interfaces = [
    {'description': 'inband mgmt interface', 'device': 1,
        'enabled': True, 'name': 'irb.255', 'type': 0, 'mgmt_only': True},
    {'description': 'inband mgmt interface', 'device': 2,
        'enabled': True, 'name': 'irb.255', 'type': 0, 'mgmt_only': True},
    {'description': 'inband mgmt interface', 'device': 3,
        'enabled': True, 'name': 'irb.255', 'type': 0, 'mgmt_only': True},
]


def send_request(netbox_url, netbox_port, netbox_token, interfaces):
    # 01: Device Interface
    # POST http://docker-01:32774/api/dcim/interfaces/

    for iface in interfaces:
        try:
            response = requests.post(
                url="http://{}:{}/api/dcim/interfaces/".format(
                    netbox_url, netbox_port),
                headers={
                    "Authorization": "Token {}".format(netbox_token),
                    "Content-Type": "application/json; charset=utf-8",
                },
                data=json.dumps({
                    "description": iface['description'],
                    "device": iface['device'],
                    "enabled": iface['enabled'],
                    "name": iface['name'],
                    "type": iface['type'],
                    "mgmt_only": iface['mgmt_only']
                })
            )
            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('Response HTTP Response Body: {content}'.format(
                content=response.content))
        except requests.exceptions.RequestException:
            print('HTTP Request failed')


if __name__ == "__main__":
    send_request(netbox_url, netbox_port, netbox_token, interfaces)
    print('all done')
