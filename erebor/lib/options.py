from argparse import ArgumentParser
from typing import List


class Options:

    def __init__(self):
        self.parser = None
        self.unknown = None
        self.known = None

        self.initial()

    def initial(self):
        self.parser = ArgumentParser(usage='./bin/places')
        self.parser.add_argument('-n', '--number', default=0, dest='number', type=int,
                                 help='Calculate distance for N random places.')

    def parse(self, args: List[str] = None):
        self.known, self.unknown = self.parser.parse_known_args(args)[:]
        if len(self.unknown) != 0:
            print(f'Unknown args received: {repr(self.unknown)}')
