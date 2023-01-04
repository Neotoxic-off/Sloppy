import requests

from src.Logger.Logger import Logger
from src.Client.Methods import Methods

class Payload:
    def __init__(self, url, method, headers, body):
        self.url = url
        self.method = method
        self.headers = headers
        self.body = body

        self.Methods = Methods()

        self.__verify_method__()
        self.__verify_body__()

    def __verify_method__(self):
        self.method = Methods.convert(self.method, self.body)

    def __verify_body__(self):
        if (self.method == "GET" and self.body != None):
            self.body = None

class Call:
    def __init__(self):
        self.Methods = Methods()
        self.Logger = Logger()

        self.bind = {
            "GET": requests.get,
            "POST": requests.post,
            "PUT": requests.put,
            "DELETE": requests.delete
        }

    def send(self, url: str, method: str, headers: dict, body: dict):
        result = self.bind[method](url, headers = headers, json = body)
        
        self.Logger.log("done", "{} {} {}".format(
            method,
            result.status_code,
            url
        ))

        return (result)

        
