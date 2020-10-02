# -*- coding: utf-8 -*-
#
#  Copyright (c) 2020 Tuono, Inc
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#
import json
import requests


class Tuono(object):
    """
    Example client to the Tuono API.

    Login options:
        token:               Use a JWT that was provided as part of another login.  Can also be copied from
                             an active browser session.
        username/password:   Provide a username and password combination and we'll go get the token
                             for you.

    Attributes:
        api_base:    The base_url to the Tuono API.  Default: https://portal.tuono.io/api.v1
        password:    The password for the Tuono user.  Only required if token is not provided.
        token:       The user's JWT token for the Tuono API.  The result of a previous login.  Not needed if
                     username and password are provided.
        username:    The user to login as.  Only required if the token is not provided.

    """
    def __init__(self, username=None, password=None, token=None, api_base="https://portal.tuono.io/api.v1"):
        self.api_base = api_base

        if token is None:
            if username is None or password is None:
                raise ValueError("Must provide either a token, or a username and password.")

            self.token = self._login(username, password)
        else:
            self.token = token

        self.headers = {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}

    def _login(self, username, password):
        headers = {"Content-Type": "application/json"}
        data = {"username": username, "password": password}
        url = f"{self.api_base}/auth/login"
        response = requests.post(url, headers=headers, data=json.dumps(data))
        token = response.json()["object"]["token"]

        return token

    def apply_environment(self, environment_id):
        """
        Apply an Environment to your cloud provider.

        Params:
            environment_id:  The ID of the environment to apply.

        Returns:
             A Job object.  The Job object can be used to track the status of the apply job.
        """
        url = f"{self.api_base}/job"
        data = dict(action="apply", environment_id=environment_id)
        response = requests.post(url, data=json.dumps(data), headers=self.headers)
        return response.json()["object"]

    def destroy_environment(self, environment_id):
        """
        Destroy an Environment in your cloud provider.

        Params:
            environment_id:  The ID of the environment to destroy.

        Returns:
             A Job object.  The Job object can be used to track the status of the destroy job.
        """
        url = f"{self.api_base}/job"
        data = dict(action="destroy", environment_id=environment_id)
        response = requests.post(url, data=json.dumps(data), headers=self.headers)
        return response.json()["object"]

    def get_blueprints(self):
        """
        Get a list of Blueprints that you have access to.

        Returns:
             A list of Blueprint objects.
        """
        url = f"{self.api_base}/blueprints"
        response = requests.get(url, headers=self.headers)
        return response.json()["objects"]

    def get_environments(self):
        """
        Get a list of Environments that you have access to.

        Returns:
             A list of Environment objects.
        """
        url = f"{self.api_base}/environments"
        response = requests.get(url, headers=self.headers)
        return response.json()["objects"]

    def get_job_status(self, job_id):
        """
        Get details for a specific Job.

        Params:
            job_id:   ID of the Job to get details for.

        Returns:
             A Job object.
        """
        url = f"{self.api_base}/job/{job_id}"
        response = requests.get(url, headers=self.headers)
        return response.json()["object"]

    def preview_environment(self, environment_id):
        """
        Preview an Environment in your cloud provider.

        Params:
            environment_id:  The ID of the environment to preview.

        Returns:
             A Job object.  The Job object can be used to track the status of the preview job.
        """
        url = f"{self.api_base}/job"
        data = dict(action="simulate", environment_id=environment_id)
        response = requests.post(url, data=json.dumps(data), headers=self.headers)
        return response.json()["object"]
