import requests


class PypiResponse():
    def __init__(self, name, version=None):
        self.name = name
        self.version = version

    def request_package_response(self):
        if self.version == None:
            response = requests.get(f'https://pypi.org/pypi/{self.name}/json')
        else :
            response = requests.get(f'https://pypi.org/pypi/{self.name}/{self.version}/json')
        return response

    def get_version(self):
        if self.version == "":
            return self.version
        else:
            self.version = self.request_package_response().json["info"]["version"]
            return self.version

    def is_valid_package(self):
        return self.request_package_response().status_code == 200
