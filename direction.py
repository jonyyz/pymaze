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
        """Get the direction value based on the name text."""
        if not isinstance(text, str):
            raise TypeError

        """Resolve the direction ordinal from the text string."""
        result = list(filter(lambda value: value == text, Direction.DIRECTION_NAMES))

        if len(result) == 0:
            return None

        return result[0]

    @staticmethod
    def getName(value):
        """Get the name text for the value."""
        if value < 0 or value > Direction.MAX:
            return None

        return Direction.DIRECTION_NAMES[value]

    @staticmethod
    def getOppositeDirection(direction):
        """Get the opposite direction."""
        oppositeDirection = direction + 2

        if oppositeDirection > Direction.MAX:
            oppositeDirection -= Direction.MAX + 1

        return oppositeDirection
