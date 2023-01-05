from src.Client.Client import Client
from src.Logger.Logger import Logger
from src.Core.Configuration import Configuration
from src.Core.Records import Records

class Engine:
    def __init__(self):
        self.Client = Client()
        self.Logger = Logger()
        self.Configuration = Configuration()
        self.Records = Records()

        self.__run__()

    def __run__(self):
        records = {}
        result = None
        data = {}

        self.Logger.log("wait", "executing payloads...")
        self.Logger.log("wait", "recording results...")
        for payload in self.Configuration.payloads:
            for action in payload["actions"]:
                result = self.Client.Call.send("{}{}".format(
                        payload["url"],
                        action["route"]
                    ),
                    action["method"],
                    self.__concat__(payload["headers"], action["headers"]),
                    self.__concat__(payload["body"], action["body"])
                )
                data = {
                    "url": result.url,
                    "method": action["method"],
                    "code": result.status_code,
                    "headers": self.__convert__(result.headers),
                    "cookies": result.cookies.get_dict(),
                    "content": result.text,
                    "history": result.history
                }

                if (payload["name"] not in records):
                    records[payload["name"]] = []
                records[payload["name"]].append(data)

        self.Logger.log("done", "results recorded")
        self.Logger.log("done", "all payloads executed")

        self.__save__(records)

    def __save__(self, records):
        self.Logger.log("wait", "saving records...")
        for record in records:
            self.Records.save(record, records[record])
        self.Logger.log("done", "records saved")

    def __convert__(self, headers):
        clean = {}

        for header in headers.keys():
            clean[header] = headers[header]
        return (clean)

    def __concat__(self, static, action):
        for key in action.keys():
            static[key] = action[key]

        return (static)