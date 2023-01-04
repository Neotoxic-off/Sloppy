class Methods:
    def __init__(self):
        self.GET = "GET"
        self.POST = "POST"
        self.PUT = "PUT"
        self.DELETE = "DELETE"

    @staticmethod
    def convert(self, data: str):
        methods = [
            self.GET,
            self.POST,
            self.PUT,
            self.DELETE
        ]

        for i in methods:
            if (data == i):
                return (i)
        return (None)