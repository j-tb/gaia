# Install the Python Requests library:
# `pip install requests`

import requests
import json


def send_request():
    # POST launch unprovision
    # POST http://tower/api/v2/job_templates/17/launch/

    try:
        response = requests.post(
            url="http://tower/api/v2/job_templates/17/launch/",
            headers={
                "Authorization": "Basic YWRtaW46cGFzc3dvcmQ=",
                "Content-Type": "application/json; charset=utf-8",
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
        return(response.status_code)
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


