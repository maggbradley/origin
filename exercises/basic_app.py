import HW
import FN
import lessons.strings as l1
import argparse
import logging
import sys

import feature as ft

# echo file to console
class App():

    def __init__(self):
        # Setup command line parsing
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--infile", help="What features to run", required=True)
        params = self.parser.parse_args()

        # Setup logging just to console
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(message)s',
                            handlers=[logging.StreamHandler(sys.stdout),
        ])





    def start(self):

        logging.info(f"Started load_file")


        logging.info(f"Ended load_file")


if __name__ == "__main__":
    myapp = App()
    myapp.start()

