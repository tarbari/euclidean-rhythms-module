from enum import Enum, auto

from pattern import Pattern


class Direction(Enum):
    FORWARDS = auto
    BACKWARDS = auto


class UserChoice(Enum):
    INCREASE_STEP = "i"
    DECREASE_STEP = "d"
    NEXT_PATTERN = "n"
    PREVIOUS_PATTERN = "p"
    ROTATE_FORWARDS = "f"
    ROTATE_BACKWARDS = "b"


def construct_visual_pattern(pattern: list[int]) -> dict[str, list[str]]:
    pattern_string = []
    for i in pattern:
        if i == 1:
            pattern_string.append("H")
        if i == 0:
            pattern_string.append("_")

    play_track = ["^" if i == 0 else " " for i in range(len(pattern_string))]

    return {"pattern_string": pattern_string, "play_track": play_track}


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


def create_pattern(hits: int, steps: int) -> Pattern:
    """Creates an euclidean rhythm pattern.

    Source: https://rosettacode.org/wiki/Euclidean_rhythm#Python

    Args:
        hits: This many events to distribute
        steps: over this many steps.

    Returns:
        A list where 1 means an event occurs and 0 means no event occurs.

    Raises:
        ValueError: In case hits > steps. This makes no sense in this application.
    """
    if hits > steps:
        raise ValueError("k must be less or equal to n.")

    s = [[1] if i < hits else [0] for i in range(steps)]

    d = steps - hits
    steps = max(hits, d)
    hits = min(hits, d)
    z = d

    while z > 0 or hits > 1:
        for i in range(hits):
            s[i].extend(s[len(s) - 1 - i])
        s = s[:-hits]
        z = z - hits
        d = steps - hits
        steps = max(hits, d)
        hits = min(hits, d)

    pattern = [item for sublist in s for item in sublist]
    v_pattern = construct_visual_pattern(pattern)

    return Pattern(pattern, v_pattern["pattern_string"], v_pattern["play_track"])
