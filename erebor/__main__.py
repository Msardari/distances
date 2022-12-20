import sys
from typing import List

from lib import Options


def main(args: List[str]) -> int:
    options = Options()
    options.parse(args[1:])

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
