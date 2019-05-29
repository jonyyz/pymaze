"""Defines the player."""


from direction import Direction


class Player:
    """Defines the player."""

    def __init__(self, name, startLocation):
        """Initialize the Player."""
        self.__name = name
        self.__location = startLocation
        self.__facingDirection = Direction.NORTH

    @property
    def name(self):
        """Get the player's name."""
        return self.__name

    @property
    def location(self):
        """Get the player's location."""
        return self.__location

    @location.setter
    def location(self, value):
        """Set the player's location."""
        self.__location = value

    @property
    def facingDirection(self):
        """Get the direction that the player is facing."""
        return self.__facingDirection

    @property
    def facingDirectionName(self):
        """Get the name of the direction that the player is facing."""
        return Direction.getName(self.facingDirection)

    def turnLeft(self):
        """Make the player face to the direction to the left."""
        if self.__facingDirection == 0:
            self.__facingDirection = Direction.MAX
        else:
            self.__facingDirection -= 1

    def turnRight(self):
        """Make the player face to the direction to the right."""
        if self.__facingDirection == Direction.MAX:
            self.__facingDirection = 0
        else:
            self.__facingDirection += 1
