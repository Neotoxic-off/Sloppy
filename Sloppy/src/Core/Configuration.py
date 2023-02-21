import json

from src.Tools.File import File
from src.Logger.Logger import Logger
from src.Models.Payload import Payload
from src.Models.Actions import Actions
from src.Models.Automatisms import Automatisms

class Configuration:
    def __init__(self):
        self.path = "payloads"
        self.extension = "json"
        self.valid = True
        self.payloads = []
        self.File = File()
        self.Payload = Payload()
        self.Logger = Logger()
        self.Actions = Actions()
        self.Automatisms = Automatisms()

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
            result = self.validate(payload)
            if (result["waited"] == None):
                self.Logger.log("done", "payload '{}' valid".format(payload["name"]))
            else:
                self.Logger.log("fail", "payload {} not valid:\n\t waited: '{}' got: '{}'".format(
                    i,
                    result["waited"],
                    result["got"],
                ))
                self.valid = False

        if (self.valid == True):
            self.Logger.log("done", "all payloads validated")

    def __sub__(self, base, payload):
        raw = base.__dict__

        for element in raw:
            if (element in payload.keys()):
                if (type(payload[element]) != raw[element]):
                    return ({
                        "waited": f"{element}: {raw[element]}",
                        "got": f"{element}: {type(payload[element])}"
                    })
            else:
                return ({
                    "waited": element,
                    "got": "not found"
                })
        return ({
            "waited": None,
            "got": None
        })

    def __check__(self, base, payload):
        raw = base.__dict__
        result = None
        bind = {
            "actions": self.Actions,
            "automatisms": self.Automatisms
        }

        for element in raw:
            if (element in payload.keys()):
                if (element in bind):
                    for sub in payload[element]:
                        result = self.__sub__(bind[element], sub)
                        if (result["waited"] != None or result["got"] != None):
                            return (result)
                elif (type(payload[element]) != raw[element]):
                    return ({
                        "waited": f"{element}: {raw[element]}",
                        "got": f"{element}: {type(payload[element])}"
                    })
            else:
                return ({
                    "waited": element,
                    "got": "not found"
                })
        return ({
            "waited": None,
            "got": None
        })

    def validate(self, payload):
        return (self.__check__(self.Payload, payload))