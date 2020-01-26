# Install the Python Requests library:
# `pip install requests`

import requests
import json


netbox_url = "docker-01"
netbox_port = "32775"
netbox_token = "0123456789abcdef0123456789abcdef01234567"
devices = [
    {'site': 1, 'device_role': 1, 'name': 'hoth', 'device_type': 2},
    {'site': 1, 'device_role': 3, 'name': 'tatooine', 'device_type': 1},
    {'site': 1, 'device_role': 3, 'name': 'dantooine', 'device_type': 3}
]


def send_request(netbox_url, netbox_port, netbox_token, devices):
    # 01: Create Site
    # POST http://docker-01:32774/api/dcim/devices/

    for device in devices:
        try:
            response = requests.post(
                url="http://{}:{}/api/dcim/devices/".format(
                    netbox_url, netbox_port),
                headers={
                    "Authorization": "Token {}".format(netbox_token),
                    "Content-Type": "application/json; charset=utf-8",
                },
                data=json.dumps({
                    "site": device['site'],
                    "device_role": device['device_role'],
                    "name": device['name'],
                    "device_type": device['device_type']
                })
            )
            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('Response HTTP Response Body: {content}'.format(
                content=response.content))
        except requests.exceptions.RequestException:
            print('HTTP Request failed')


if __name__ == "__main__":
    send_request(netbox_url, netbox_port, netbox_token, devices)
    print('all done')
