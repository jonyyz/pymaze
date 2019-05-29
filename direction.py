"""Defines the direction enumeration."""


class Direction:
    """Cardinal direction values."""

    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    MAX = WEST

    DIRECTION_NAMES = ["north", "east", "south", "west"]

    @staticmethod
    def getValue(text):
        """Resolve the direction ordinal from the text string."""
        result = list(filter(lambda value: value == text, Direction.DIRECTION_NAMES))

        if len(result) == 0:
            return None

        return result[0]

    @staticmethod
    def getName(direction):
        """Get the name text for the value."""
        if direction < 0 or direction > Direction.MAX:
            return None

        return Direction.DIRECTION_NAMES[direction]

    @staticmethod
    def getOppositeDirection(direction):
        """Get the opposite direction."""
        oppositeDirection = direction + 2

        if oppositeDirection > Direction.MAX:
            oppositeDirection -= Direction.MAX + 1

        return oppositeDirection
