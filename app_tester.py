import HW
import FN
import feature as ft
class App():
    def __init__(self):
        self.handler_list = {
            "HW": ft.Feature("Hello world", HW.handler),
            "FN": ft.Feature("Abraham", FN.handler)
        }
        self.handler_to_run = "FN"


    def start(self):

        print('Starting app_tester')

        feat = self.handler_list[self.handler_to_run]
        feat.run()

        print('app_tester completed')


if __name__ == "__main__":
    myapp = App()
    myapp.start()

