class Feature():
    def __init__(self, name, handler):
        self.name = name
        self.handler = handler

    def run(self):
        try:
            self.handler()
        except:
            print(f"handler func: {self.name} FAILED!!")


