from src.Client.Client import Client
from src.Logger.Logger import Logger
from src.Core.Configuration import Configuration

class Engine:
    def __init__(self):
        self.Client = Client()
        self.Logger = Logger()
        self.Configuration = Configuration()

        self.__run__()

    def __run__(self):
        result = None
    
        self.Logger.log("wait", "executing payloads...")
        for payload in self.Configuration.payloads:
            for action in payload["actions"]:
                result = self.Client.Call.send("{}{}".format(
                        payload["url"],
                        action["route"]
                    ),
                    action["method"],
                    action["headers"],
                    action["body"]
                )
        self.Logger.log("done", "all payloads executed")


