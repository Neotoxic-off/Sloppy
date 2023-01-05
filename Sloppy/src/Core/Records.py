import os
import json
import datetime

from src.Tools.File import File

class Records:
    def __init__(self):
        self.folder = "records"

        self.File = File()

        self.__build__()

    def __build__(self):
        if (os.path.exists(self.folder) == False):
            os.mkdir(self.folder)

    def save(self, name: str, record: dict):
        self.File.save("{}/{}_{}.json".format(
            self.folder,
            name,
            datetime.datetime.now().strftime("%m%d%Y%M%S")
        ), record)
        