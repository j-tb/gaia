# Install the Python Requests library:
# `pip install requests`

import requests
import json


netbox_url = "docker-01"
netbox_port = "32775"
netbox_token = "0123456789abcdef0123456789abcdef01234567"
manufacturers = [
    {'manufacturer_name': 'juniper', 'manufacturer_slug': 'juniper'},
    {'manufacturer_name': 'cisco', 'manufacturer_slug': 'cisco'},
    {'manufacturer_name': 'vmware', 'manufacturer_slug': 'vmware'}
]


def send_request(netbox_url, netbox_port, netbox_token, manufacturers):
    # 01: Create Site
    # POST http://docker-01:32774/api/dcim/manufacturers/

    for manufacturer in manufacturers:
        try:
            response = requests.post(
                url="http://{}:{}/api/dcim/manufacturers/".format(
                    netbox_url, netbox_port),
                headers={
                    "Authorization": "Token {}".format(netbox_token),
                    "Content-Type": "application/json; charset=utf-8",
                },
                data=json.dumps({
                    "name": manufacturer['manufacturer_name'],
                    "slug": manufacturer['manufacturer_slug']
                })
            )
            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('Response HTTP Response Body: {content}'.format(
                content=response.content))
        except requests.exceptions.RequestException:
            print('HTTP Request failed')


if __name__ == "__main__":
    send_request(netbox_url, netbox_port, netbox_token, manufacturers)
    print('all done')
