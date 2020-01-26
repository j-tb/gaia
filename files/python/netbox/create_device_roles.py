# Install the Python Requests library:
# `pip install requests`

import requests
import json


netbox_url = "docker-01"
netbox_port = "32775"
netbox_token = "0123456789abcdef0123456789abcdef01234567"
device_roles = [
    {'role_name': 'firewall', 'role_slug': 'firewall', 'role_color': '55564f'},
    {'role_name': 'router', 'role_slug': 'router', 'role_color': '525867'},
    {'role_name': 'switch', 'role_slug': 'switch', 'role_color': '818da3'},
    {'role_name': 'linux', 'role_slug': 'linux', 'role_color': 'cc9092'},
    {'role_name': 'windows', 'role_slug': 'windows', 'role_color': 'dbd2cd'}
]


def send_request(netbox_url, netbox_port, netbox_token, device_roles):
    # 01: Create Site
    # POST http://docker-01:32774/api/dcim/device-roles/

    for role in device_roles:
        try:
            response = requests.post(
                url="http://{}:{}/api/dcim/device-roles/".format(
                    netbox_url, netbox_port),
                headers={
                    "Authorization": "Token {}".format(netbox_token),
                    "Content-Type": "application/json; charset=utf-8",
                },
                data=json.dumps({
                    "name": role['role_name'],
                    "slug": role['role_slug'],
                    "color": role['role_color']
                })
            )
            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('Response HTTP Response Body: {content}'.format(
                content=response.content))
        except requests.exceptions.RequestException:
            print('HTTP Request failed')


if __name__ == "__main__":
    send_request(netbox_url, netbox_port, netbox_token, device_roles)
    print('all done')
