# Install the Python Requests library:
# `pip install requests`

import requests
import json


netbox_url = "docker-01"
netbox_port = "32775"
netbox_token = "0123456789abcdef0123456789abcdef01234567"
device_types = [
    {'manufacturer': 1, 'model': 'EX3400-24P', 'slug': 'ex3400_24p'},
    {'manufacturer': 1, 'model': 'SRX340', 'slug': 'srx340'},
    {'manufacturer': 1, 'model': 'EX2300-C-12T', 'slug': 'ex2300_C_12T'}
]


def send_request(netbox_url, netbox_port, netbox_token, device_types):
    # 01: Create Site
    # POST http://docker-01:32774/api/dcim/device-types/

    for each in device_types:
        try:
            response = requests.post(
                url="http://{}:{}/api/dcim/device-types/".format(
                    netbox_url, netbox_port),
                headers={
                    "Authorization": "Token {}".format(netbox_token),
                    "Content-Type": "application/json; charset=utf-8",
                },
                data=json.dumps({
                    "manufacturer": each['manufacturer'],
                    "model": each['model'],
                    "slug": each['slug']
                })
            )
            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('Response HTTP Response Body: {content}'.format(
                content=response.content))
        except requests.exceptions.RequestException:
            print('HTTP Request failed')


if __name__ == "__main__":
    send_request(netbox_url, netbox_port, netbox_token, device_types)
    print('all done')
