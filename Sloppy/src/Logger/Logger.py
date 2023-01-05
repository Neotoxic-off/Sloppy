class Logger:
    def __init__(self):
        self.bind = {
            "wait": {
                "display": "[ WAIT ]",
                "color": "yellow"
            },
            "done": {
                "display": "[ DONE ]",
                "color": "green"
            },
            "fail": {
                "display": "[ FAIL ]",
                "color": "red"
            },
            "action": {
                "display": "\t-->",
                "color": "yellow"
            }
        }
        self.colors = {
            "red": "\033[31m",
            "white": "\033[37m",
            "green": "\033[32m",
            "yellow": "\033[33m",
            "reset": "\033[0m"
        }

    def log(self, _type: str, message: str):
        print("{}{}{} {}".format(
            self.colors[self.bind[_type]["color"]],
            self.bind[_type]["display"],
            self.colors["reset"],
            message
        ))
