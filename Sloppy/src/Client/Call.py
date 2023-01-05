import requests

from src.Logger.Logger import Logger

class Call:
    def __init__(self):
        self.Logger = Logger()

        self.bind = {
            "GET": requests.get,
            "POST": requests.post,
            "PUT": requests.put,
            "DELETE": requests.delete
        }

    def send(self, url: str, method: str, headers: dict, body: dict):
        result = self.bind[method](url, headers = headers, json = body)
        
        self.Logger.log("action", "{} {} {}".format(
            method,
            result.status_code,
            url
        ))

        return (result)

        
