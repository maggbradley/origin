import HW
import feature as ft
class App():
    def __init__(self):
        self.handler_list = {
            "HW": ft.Feature("Hello world", HW.handler),

        }
        self.handler_to_run = "HW"

    def start(self):

        print('Starting app_tester')

        feat = self.handler_list[self.handler_to_run]
        feat.run()

        print('app_tester completed')


if __name__ == "__main__":
    myapp = App()
    myapp.start()

