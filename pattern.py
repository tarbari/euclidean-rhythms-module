from dataclasses import dataclass

from direction import Direction


@dataclass
class Pattern:
    pattern: list[int]
    pattern_track: list[str]
    playhead_track: list[str]
    playhead_pos: int = 0

    def rotate_pattern(self, direction: Direction = Direction.FORWARDS) -> None:
        """Rotates the pattern one step to the specified direction.

        Args:
            rotation: Direction of rotation. Defaults to forwards.
        """

        match direction:
            case Direction.FORWARDS:
                self.pattern.insert(0, self.pattern.pop())
            case Direction.BACKWARDS:
                self.pattern.append(self.pattern.pop(0))

    def print_pattern(self) -> None:
        """Assumes mono spaced font."""
        # for c in self.pattern_track:
        #     print(c, end="\r")
        # print()
        # for c in self.playhead_track:
        #     print(c, end="\r")
        print("".join(self.pattern_track))
        # print(f"Playhead position: {self.playhead_pos}")
        # print()
        #

    def print_playhead(self) -> None:
        print("".join(self.playhead_track), end="\r")

    def move_playhead(self) -> None:
        if self.playhead_pos >= len(self.playhead_track) - 1:
            self.playhead_pos = 0
        else:
            self.playhead_pos += 1

        self.playhead_track.insert(0, self.playhead_track.pop())
