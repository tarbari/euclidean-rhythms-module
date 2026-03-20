from enum import Enum, auto


class Direction(Enum):
    FORWARDS = auto
    BACKWARDS = auto

    
class UserChoice(Enum):
    INCREASE_STEP = 'i'
    DECREASE_STEP = 'd'
    NEXT_PATTERN = 'n'
    PREVIOUS_PATTERN = 'p'
    ROTATE_FORWARDS = 'f'
    ROTATE_BACKWARDS = 'b'
