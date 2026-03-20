import argparse

from time import sleep

from pattern import Pattern
from utils import UserChoice




def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--events", "-e", type=int, default=4)
    parser.add_argument("--steps", "-s", type=int, default=16)
    parser.add_argument("--rotation", "-r", type=int, default= 0)
    return parser.parse_args()


def create_pattern(k: int, n: int) -> Pattern:
    """Creates an euclidean rhythm pattern.

    Source: https://rosettacode.org/wiki/Euclidean_rhythm#Python

    Args:
        k: This many events to distribute
        n: over this many steps.

    Returns:
        A list where 1 means an event occurs and 0 means no event occurs.

    Raises:
        ValueError: In case k > n. This makes no sense in this application.
    """
    if k > n:
        raise ValueError("k must be less or equal to n.")

    s = [[1] if i < k else [0] for i in range(n)]

    d = n - k
    n = max(k, d)
    k = min(k, d)
    z = d

    while z > 0 or k > 1:
        for i in range(k):
            s[i].extend(s[len(s) - 1 - i])
        s = s[:-k]
        z = z - k
        d = n - k
        n = max(k, d)
        k = min(k, d)

    pattern = [item for sublist in s for item in sublist]
    v_pattern = construct_visual_pattern(pattern)

    return Pattern(
        pattern,
        v_pattern["pattern_string"],
        v_pattern["play_track"]
    )




def read_input() -> UserChoice:
    while True:
        try:
            i = input("Choice: ")
            c = UserChoice(i)
            return c
        except ValueError as e:
            print(f"Invalid value: {e}")


def print_menu() -> None:
    print("Press 'i' to increase step and 'd' to decrease step.")
    print("Press 'n' to increase events and 'p' to decrease events.")
    print("Press 'f' to rotate events forwards and 'b' to rotate events backwards.")


def construct_visual_pattern(pattern: list[int]) -> dict[str, list[str]]:
    pattern_string = []
    for i in pattern:
        if i == 1:
            pattern_string.append("H")
        if i == 0:
            pattern_string.append("_")

    play_track = ["^" if i == 0 else " " for i in range(len(pattern_string))]

    return {
        "pattern_string": pattern_string,
        "play_track": play_track
    }


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
    
