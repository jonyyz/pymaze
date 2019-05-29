"""Coordinates."""


class Coordinates:
    """Define a 2D coordinates object."""

    def __init__(self, x, y):
        """Initialize a Coordinates object from 2D coordinate values."""
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError

        self.__x = x
        self.__y = y

    def __str__(self):
        """Get a string representation of the object."""
        return f"X={self.__x},Y={self.__y}"

    @property
    def x(self):
        """Get the X coordinate."""
        return self.__x

    @property
    def y(self):
        """Get the Y coordinate."""
        return self.__y
