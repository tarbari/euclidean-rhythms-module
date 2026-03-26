import argparse
from time import sleep

from utils import create_pattern


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--events", "-e", type=int, default=4)
    parser.add_argument("--steps", "-s", type=int, default=16)
    parser.add_argument("--rotation", "-r", type=int, default=0)
    return parser.parse_args()


def main(args: argparse.Namespace):
    events = args.events
    steps = args.steps
    pattern = create_pattern(events, steps)

    pattern.print_pattern()
    for _ in range(len(pattern.pattern) * 2):
        pattern.print_playhead()
        pattern.move_playhead()
        sleep(0.1)


if __name__ == "__main__":
    args = parse_args()
    main(args)
