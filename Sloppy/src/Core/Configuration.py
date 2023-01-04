import json

from src.Tools.File import File
from src.Logger.Logger import Logger

class Model:
    def __init__(self):
        self.requirements = [
            {
                "name": "url",
                "type": str
            },
            {
                "name": "headers",
                "type": dict
            },
            {
                "name": "body",
                "type": dict
            },
            {
                "name": "actions",
                "type": list
            },
        ]
        self.action = [
            {
                "name": "route",
                "type": str
            },
            {
                "name": "method",
                "type": str
            },
            {
                "name": "headers",
                "type": dict
            },
            {
                "name": "body",
                "type": dict
            },
        ]

    def __actions__(self, actions: list):
        for action in actions:
            for default in self.action:
                if (default["name"] in action):
                    if (type(action[default["name"]]) != default["type"]):
                        return ({
                            "waited": default["type"],
                            "got": type(action[default["name"]])
                        })
                else:
                    return ({
                        "waited": default["name"],
                        "got": "not found"
                    })
        return ({
            "waited": None,
            "got": None
        })

    def validate(self, payload):
        result = None
    
        for element in self.requirements:
            if (element["name"] in payload):
                if (type(payload[element["name"]]) != element["type"]):
                    return ({
                        "waited": element["type"],
                        "got": type(payload[element["name"]])
                    })
                elif (element["name"] == "actions"):
                    result = self.__actions__(payload[element["name"]])
                    if (result["waited"] != None):
                        return (result)
            else:
                return ({
                    "waited": element["name"],
                    "got": "not found"
                })
        return ({
            "waited": None,
            "got": None
        })

class Configuration:
    def __init__(self):
        self.path = "payloads"
        self.extension = "json"
        self.payloads = []
        self.File = File()
        self.Model = Model()
        self.Logger = Logger()

        self.__build__()
        self.__parse__()

    def __build__(self):
        files = self.File.search(self.path, self.extension)

        self.Logger.log("wait", "loading payloads...")
        for _file in files:
            self.payloads.append(
                json.loads(
                    self.File.load("{}/{}".format(self.path, _file))
                )
            )
        self.Logger.log("done", f"{len(self.payloads)} payloads loaded")

    def __parse__(self):
        result = None
        self.Logger.log("wait", "checking payloads...")

        for i, payload in enumerate(self.payloads):
            result = self.Model.validate(payload)
            if (result["waited"] == None):
                self.Logger.log("done", "payload {} valid".format(i))
            else:
                self.Logger.log("fail", "payload {} not valid: waited: '{}' got: '{}'".format(
                    i,
                    result["waited"],
                    result["got"],
                ))

        self.Logger.log("done", "all payloads checked")
        
            