"""Definition of the maze that the player will be in."""


import os

from coordinates import Coordinates
from direction import Direction


class Map:
    """Map definition."""

    MAP_DIR = "./maps"
    WIDTH = 32
    HEIGHT = 32
    TILE_OUTSIDE_MAP = chr(9618)

    @staticmethod
    def __createEmptyMap():
        """Create an empty map."""
        return [[None for x in range(Map.WIDTH)] for y in range(Map.HEIGHT)]

    def __init__(self, name):
        """Initialize the map."""
        self.__startLocation = None
        self.__exitLocation = None

        map = Map.__createEmptyMap()
        y = 0

        with open(
                os.path.join(self.MAP_DIR, f"{name}.map"),
                "r",
                encoding="utf8"
                ) as f:
            for line in f:
                x = 0
                for ch in line.rstrip(os.linesep):
                    map[y][x] = ch

                    if ch == "S":
                        self.__startLocation = Coordinates(x, y)
                    elif ch == "E":
                        self.__exitLocation = Coordinates(x, y)

                    x += 1
                y += 1
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

    def __getTileAtCoordinates(self, coordinates):
        """Get the map tile specified by the coordinates."""
        x = coordinates.x
        y = coordinates.y

        # Check if the coordinates are out of the bounds of the map
        if x < 0 or x > Map.WIDTH or y < 0 or y > Map.HEIGHT:
            return None

        return self.__map[y][x]

    def getDestinationInDirectionFromLocation(
        self,
        originLocation,
        moveDirection
    ):
        """Get the location that is adjacent to the direction's location."""
        originTile = self.__getTileAtCoordinates(originLocation)

        if originTile == Map.TILE_OUTSIDE_MAP:
            return None

        x = originLocation.x
        y = originLocation.y

        if moveDirection == Direction.NORTH:
            y -= 1
        elif moveDirection == Direction.EAST:
            x += 1
        elif moveDirection == Direction.SOUTH:
            y += 1
        elif moveDirection == Direction.WEST:
            x -= 1

        destinationLocation = Coordinates(x, y)
        destinationTile = self.__getTileAtCoordinates(destinationLocation)

        return None if destinationTile == Map.TILE_OUTSIDE_MAP else destinationLocation

    def getViewableArea(self, originLocation, direction):
        """Get the viewable area from the origin location facing the direction."""
        viewableDepth = 4
        viewableWidth = 3

        # Initialize the viewable area to be all outside the map
        viewableArea = [[Map.TILE_OUTSIDE_MAP for x in range(viewableWidth)] for y in range(viewableDepth)]

        originX = originLocation.x
        originY = originLocation.y

        writeX = None
        writeY = None

        if direction == Direction.NORTH:
            writeX = 0
            writeY = viewableDepth - 1

            for readY in reversed(range(originY - viewableDepth + 1, originY + 1)):
                if readY < 0:
                    break

                for readX in range(originX - 1, originX + 2):
                    if readX in range(0, Map.WIDTH):
                        # print(f"readX={readX},readY={readY},writeX={writeX},writeY={writeY}")
                        viewableArea[writeY][writeX] = self.__map[readY][readX]
                    writeX += 1
                writeY -= 1
                writeX = 0

        return viewableArea
