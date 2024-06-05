import HW
import FN
import lessons.strings as l1
import argparse
import logging
import sys

import feature as ft

# clps
#   infile
#   outfile
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



    def load_file(self):
        return lines

    def save_file

    def start(self):

        logging.info(f"Started load_file")
    def loadFile(infile):
        logging.info(f"Starting to copy")
        with open(infile, "r") as file:
            data = file.read()
            print(data)
            return data

    def numLines(infile):
       with open(infile, "r") as file:
           f = file.readlines()
           l = len(f)
           print(l)
        logging.info({l} lines read)

    def saveFile(outfile):
        logging.info(f"Starting to save")
        with open(infile, "r") as rf:
            file_contents = file.read()
            le = len(file_contents)
            print(le)
        with open(outfile, "w") as file:
            print(file_contents)
            file.write(file_contents)
        logging.info(f"Saved {le} lines") 

        logging.info(f"Ended load_file")


if __name__ == "__main__":
    myapp = App()
    myapp.start()

