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

    # while True:
    #     print_menu()
    #
    #     v_pattern = construct_visual_pattern(pattern)
    #     print_pattern(v_pattern)
    #
    #
    #     match read_input():
    #         case UserChoice.INCREASE_STEP:
    #             steps += 1
    #             pattern = create_pattern(events, steps)
    #
    #         case UserChoice.DECREASE_STEP:
    #             steps -= 1
    #             pattern = create_pattern(events, steps)
    #
    #         case UserChoice.NEXT_PATTERN:
    #             events += 1
    #             pattern = create_pattern(events, steps)
    #
    #         case UserChoice.PREVIOUS_PATTERN:
    #             events -= 1
    #             pattern = create_pattern(events, steps)
    #
    #         case UserChoice.ROTATE_FORWARDS:
    #             rotate_pattern(pattern)
    #
    #         case UserChoice.ROTATE_BACKWARDS:
    #             rotate_pattern(pattern, Direction.BACKWARDS)


if __name__ == "__main__":
    args = parse_args()
    main(args)
