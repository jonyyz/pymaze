"""Definition of the maze that the player will be in."""


import os

from coordinates import Coordinates
from direction import Direction


class Map:
    """Map definition."""

    MAP_DIR = "./maps"
    WIDTH = 32
    HEIGHT = 32
    TILE_OUTSIDE_MAP = 9618

    def __init__(self, name):
        """Initialize the map."""
        self.__startLocation = None
        self.__exitLocation = None

        map = Map.__createEmptyMap()
        row = 0

        with open(
                os.path.join(self.MAP_DIR, f"{name}.map"),
                "r",
                encoding="utf8"
                ) as f:
            for line in f:
                col = 0
                for ch in line.rstrip(os.linesep):
                    map[row][col] = ch

                    if ch == "S":
                        self.__startLocation = self.translateRowAndColumnToCoordinates(row, col)
                    elif ch == "E":
                        self.__exitLocation = self.translateRowAndColumnToCoordinates(row, col)

                    col += 1
                row += 1
            self.__map = map
            f.close()

    @property
    def startLocation(self):
        """Get the starting location of the map."""
        return self.__startLocation

    @property
    def exitLocation(self):
        """Get the exit location of the map."""
        return self.__exitLocation

    def __createEmptyMap():
        """Create an empty map."""
        return [[None for x in range(Map.WIDTH)] for y in range(Map.HEIGHT)]

    def translateRowAndColumnToCoordinates(self, row, col):
        """Translate Row and Column to Coordinates"""
        return Coordinates(col, Map.WIDTH - row - 1)

    def getDestinationInDirectionFromLocation(
        self,
        originLocation,
        moveDirection
    ):
        """Get the location that is adjacent to the direction's location."""
        originTile = self.getTileAtCoordinates(originLocation)

        if ord(originTile) == Map.TILE_OUTSIDE_MAP:
            return None

        x = originLocation.x
        y = originLocation.y

        if moveDirection == Direction.NORTH:
            y += 1
        elif moveDirection == Direction.EAST:
            x += 1
        elif moveDirection == Direction.SOUTH:
            y -= 1
        elif moveDirection == Direction.WEST:
            x -= 1

        destinationLocation = Coordinates(x, y)
        destinationTile = self.getTileAtCoordinates(destinationLocation)

        return None if ord(destinationTile) == Map.TILE_OUTSIDE_MAP else destinationLocation

    def getTileAtCoordinates(self, coordinates):
        """Get the map tile specified by the coordinates."""
        x = coordinates.x
        y = coordinates.y

        # Check if the coordinates are out of the bounds of the map
        if x < 0 or x > Map.WIDTH or y < 0 or y > Map.HEIGHT:
            return None

        return self.__map[Map.WIDTH - y - 1][x]
