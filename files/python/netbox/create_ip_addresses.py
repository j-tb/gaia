# Install the Python Requests library:
# `pip install requests`

import requests
import json


netbox_url = "docker-01"
netbox_port = "32775"
netbox_token = "0123456789abcdef0123456789abcdef01234567"
ip_addresses = [
    {'interface': 1, 'dns_name': 'hoth.home',
        'description': 'irb.255 interface for inband management', 'address': '10.255.0.1/17'},
    {'interface': 2, 'dns_name': 'tatooine.home',
        'description': 'irb.255 interface for inband management', 'address': '10.255.0.11/17'},
    {'interface': 3, 'dns_name': 'dantooine.home',
        'description': 'irb.255 interface for inband management', 'address': '10.255.0.12/17'}
]


def send_request(netbox_url, netbox_port, netbox_token, ip_addresses):
    # 01: Create Site
    # POST http://docker-01:32774/api/ipam/ip-addresses/

    for ip in ip_addresses:
        try:
            response = requests.post(
                url="http://{}:{}/api/ipam/ip-addresses/".format(
                    netbox_url, netbox_port),
                headers={
                    "Authorization": "Token {}".format(netbox_token),
                    "Content-Type": "application/json; charset=utf-8",
                },
                data=json.dumps({
                    "interface": ip['interface'],
                    "dns_name": ip['dns_name'],
                    "description": ip['description'],
                    "address": ip['address']
                })
            )
            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('Response HTTP Response Body: {content}'.format(
                content=response.content))
        except requests.exceptions.RequestException:
            print('HTTP Request failed')


if __name__ == "__main__":
    send_request(netbox_url, netbox_port, netbox_token, ip_addresses)
    print('all done')
