"""Factory to create the viewport surface."""

from ..surface import Surface
from .border import border
from map import Map

viewableAreaWidth = 3
viewableAreaHeight = 4

def create(viewableArea):
    """Create the viewport surface."""
    viewPort = Surface(width=43, height=34, initChar=None)

    # Draw the border on it
    border.drawToSurface(viewPort)

    viewableAreaSurface = createViewableAreaSurface(viewableArea)
    viewableAreaSurface.drawToSurface(viewPort, x=4, y=2)

    return viewPort

#             1111111111222222222233333
#   01234567890123456789012345678901234
#  0
#  1
#  2
#  3
#  4
#  5
#  6
#  7
#  8
#  9
# 10
# 11___________ ___________ ___________
# 12           |           |
# 13           |           |
# 14           |           |
# 15           |           |
# 16           |           |
# 17           |           |
# 18___________|___________|___________
# 19
# 20
# 21
# 22
# 23
# 24
# 25
# 26
# 27
# 28
# 29
# 30

#             1111111111222222222233333
#   01234567890123456789012345678901234
#  0\                                 /
#  1 \                               /
#  2  \                             /
#  3   \                           /
#  4    \                         /
#  5     \                       /
#  6     |\                      |
#  7     | \                     |
#  8     |  \                    |
#  9     |   \               ____|
# 10     |   |\             /|   |
# 11     |   | \___________/ |   |
# 12     |   | |           | |   |
# 13     |   | |           | |   |
# 14     |   | |           | |   |
# 15     |   | |           | |   |
# 16     |   | |           | |   |
# 17     |   | |           | |   |
# 18     |   | |___________| |   |
# 19     |   | /           \ |   |
# 20     |   |/             \|___|
# 21     |   /                   |
# 22     |  /                    |
# 23     | /                     |
# 24     |/                      |
# 25     /                       \
# 26    /                         \
# 27   /                           \
# 28  /                             \
# 29 /                               \
# 30/                                 \

def drawBackLeftSurface(surface, leftTile, leftBackTile):
    """Draw the back left surface."""
    if leftTile:
        #            111
        #  0123456789012
        # 0         \
        # 1         |\
        # 2         | \
        # 3         | |
        # 4         | |
        # 5         | |
        # 6         | |
        # 7         | |
        # 8         | |
        # 9         | |
        # 10        | /
        # 11        |/
        # 12        /
        surface.plot(9, 0, "\\")
        surface.drawText(9, 1, "|\\")
        surface.drawText(9, 2, "| \\")

        for y in range(3, 10):
            surface.drawText(9, y, "| |")

        surface.drawText(9, 10, "| /")
        surface.drawText(9, 11, "|/")
        surface.plot(9, 12, "/")
    elif leftBackTile:
        #            111
        #  0123456789012
        # 0         \
        # 1         |
        # 2         |_
        # 3         | |
        # 4         | |
        # 5         | |
        # 6         | |
        # 7         | |
        # 8         | |
        # 9         |_|
        # 10        |
        # 11        |
        # 12        /
        surface.plot(9, 0, "\\")
        surface.plot(9, 1, "|")
        surface.drawText(9, 2, "|_")

        for y in range(3, 9):
            surface.drawText(9, y, "| |")

        surface.drawText(9, 9, "|_|")

        for y in range(10, 12):
            surface.plot(9, y, "|")
        surface.plot(9, 12, "/")

def drawBackCenterSurface(surface, centerTile, centerBackTile):
    """Draw the back center surface."""
    if centerTile or not centerBackTile:
        return

    #            1111111111222
    #  01234567890123456789012
    # 0
    # 1
    # 2            ___________
    # 3           |           |
    # 4           |           |
    # 5           |           |
    # 6           |           |
    # 7           |           |
    # 8           |           |
    # 9           |___________|
    # 10
    # 11
    # 12
    surface.drawText(12, 2, "___________")

    for y in range(3, 9):
        surface.drawText(11, y, "|           |")

    surface.drawText(11, 9, "|___________|")

def createBackRowSurface(currentRow, backRow):
    """Create the back row surface."""
    leftBackTile = backRow[0] == Map.TILE_OUTSIDE_MAP
    centerBackTile = backRow[1] == Map.TILE_OUTSIDE_MAP
    rightBackTile = backRow[2] == Map.TILE_OUTSIDE_MAP

    leftTile = currentRow[0] == Map.TILE_OUTSIDE_MAP
    centerTile = currentRow[1] == Map.TILE_OUTSIDE_MAP
    rightTile = currentRow[2] == Map.TILE_OUTSIDE_MAP

    width = 35
    height = 13

    surface = Surface(width=width, height=height)

    # print(f"leftTile={leftTile},leftBackTile={leftBackTile}")
    drawBackLeftSurface(surface, leftTile, leftBackTile)
    drawBackCenterSurface(surface, centerTile, centerBackTile)

    return surface

def dumpViewableArea(viewableArea):
    """Dump the viewable area for debugging."""
    y = 0
    x = 0

    print("+---+")
    for row in viewableArea:
        print("|", end="")
        for ch in row:
            print("X" if y == 3 and x == 1 else ch, end="")
            x += 1
        print("|")
        y += 1
        x = 0
    print("+---+")

def createViewableAreaSurface(viewableArea):
    """Create the viewable area surface."""
    if not isinstance(viewableArea, list):
        raise TypeError

    if len(viewableArea) != viewableAreaHeight or len(viewableArea[0]) != viewableAreaWidth:
        raise ValueError(f"Viewable area must be {viewableAreaHeight}x{viewableAreaWidth}")

    dumpViewableArea(viewableArea)

    surface = Surface(width=35, height=31)

    backRowSurface = createBackRowSurface(viewableArea[1], viewableArea[0])
    backRowSurface.drawToSurface(surface, x=0, y=9)

    return surface
