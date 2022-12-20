import sys
from typing import List

from lib import Options, Engine


def main(args: List[str]) -> int:
    options = Options()
    options.parse(args[1:])

    engine = Engine(options)

    distances = engine.get_distances().to_dict(orient='records')
    for distance in distances:
        print(f'{distance["place1"]:<25}{distance["place2"]:<25}{distance["distance"]:.1f} km')

    print('\n')

    distance_average = engine.avg()
    closest_pair = engine.closest_pair(distance_average).to_dict(orient='records')[0]

    print(f'Average distance: {distance_average:.1f} km.'
          f' Closest pair: {closest_pair["place1"]} - {closest_pair["place2"]} {closest_pair["distance"]:.1f} km.')

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
