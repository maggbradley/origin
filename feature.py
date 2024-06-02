class Feature():
    def __init__(self, name, handler, app = None):
        self.name = name
        self.handler = handler
        self.app = app

    def run(self):
        try:
            self.handler(app = self.app)
        except:
            print(f"handler func: {self.name} FAILED!!")


