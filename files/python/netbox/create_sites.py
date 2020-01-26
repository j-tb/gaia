# Install the Python Requests library:
# `pip install requests`

import requests
import json


netbox_url = "docker-01"
netbox_port = "32775"
netbox_token = "0123456789abcdef0123456789abcdef01234567"
sites = [{'site_name': 'brookefield', 'site_slug': 'brookefield'}, {
    'site_name': 'eve', 'site_slug': 'eve'}, {'site_name': 'vmware', 'site_slug': 'vmware'}]


def send_request(netbox_url, netbox_port, netbox_token, sites):
    # 01: Create Site
    # POST http://docker-01:32774/api/dcim/sites/

    for site in sites:
        try:
            response = requests.post(
                url="http://{}:{}/api/dcim/sites/".format(
                    netbox_url, netbox_port),
                headers={
                    "Authorization": "Token {}".format(netbox_token),
                    "Content-Type": "application/json; charset=utf-8",
                },
                data=json.dumps({
                    "name": site['site_name'],
                    "slug": site['site_slug']
                })
            )
            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('Response HTTP Response Body: {content}'.format(
                content=response.content))
        except requests.exceptions.RequestException:
            print('HTTP Request failed')


if __name__ == "__main__":
    send_request(netbox_url, netbox_port, netbox_token, sites)
    print('all done')
