class Logger:
    def __init__(self):
        self.bind = {
            "wait": "[ WAIT ]",
            "done": "[ DONE ]",
            "fail": "[ FAIL ]"
        }

    def log(self, _type: str, message: str):
        print("{} {}".format(
            self.bind[_type],
            message
        ))
