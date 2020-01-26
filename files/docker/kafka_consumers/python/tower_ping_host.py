# Install the Python Requests library:
# `pip install requests`

import requests
import json


route_reflectors = ["139.65.224.11", "10.255.0.2"]

def send_request(host_name):
    # POST launch unprovision
    # POST http://tower/api/v2/job_templates/15/launch/

    for neighbor in route_reflectors:
        try:
            response = requests.post(
                url="http://tower/api/v2/job_templates/15/launch/",
                headers={
                    "Authorization": "Basic YWRtaW46cGFzc3dvcmQ=",
                    "Content-Type": "application/json; charset=utf-8",
                },
                data=json.dumps({
                    "extra_vars": {
                        "host_name": host_name,
                        "neighbor": neighbor
                    }
                })
            )
            print('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            print('Response HTTP Response Body: {content}'.format(
                content=response.content))
            return(response.status_code)
        except requests.exceptions.RequestException:
            print('HTTP Request failed')


