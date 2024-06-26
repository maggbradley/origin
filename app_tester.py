import HW
import FN
import lessons.strings as l1
import argparse
import logging
import sys

import feature as ft
class App():

    def __init__(self):
        # Setup command line parsing
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--torun", help="What features to run", )
        params = self.parser.parse_args()

        # Setup logging just to console
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(message)s',
                            handlers=[logging.StreamHandler(sys.stdout),
        ])

        self.handler_list = {
            "HW": ft.Feature("Hello world", HW.handler, app=self),
            "FN": ft.Feature("Abraham", FN.handler, app=self),
            "less_1": ft.Feature("less_1", l1.tester, app=self),
        }
        self.handler_to_run = params.torun




    def start(self):

        print('Starting app_tester')

        feat = self.handler_list[self.handler_to_run]
        feat.run()

        print('app_tester completed')


if __name__ == "__main__":
    myapp = App()
    myapp.start()

