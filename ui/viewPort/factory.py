"""Factory to create the viewport surface."""

from ..surface import Surface
from .border import border
from map import Map

VIEWABLE_AREA_WIDTH = 3
VIEWABLE_AREA_HEIGHT = 4

VIEWABLE_AREA_VIEWPORT_WIDTH = 35
VIEWABLE_AREA_VIEWPORT_HEIGHT = 31

def create(viewableArea):
    """Create the viewport surface."""
    viewPort = Surface(width=43, height=34, initChar=None)

    # Draw the border on it
    border.drawToSurface(viewPort)

    viewableAreaSurface = Surface(width=VIEWABLE_AREA_VIEWPORT_WIDTH, height=VIEWABLE_AREA_VIEWPORT_HEIGHT)
    drawViewableArea(viewableAreaSurface, viewableArea)
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

def drawBackLeftFrontSurface(surface):
    """Draw the back left front surface."""
    #             11
    #   012345678901
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
    # 11___________
    # 12           |
    # 13           |
    # 14           |
    # 15           |
    # 16           |
    # 17           |
    # 18___________|
    surface.drawText(x=0, y=11, text="___________")

    for y in range(12, 18):
        surface.plot(x=11, y=y, ch="|")

    surface.drawText(x=0, y=18, text="___________|")

def drawBackLeftRightSurface(surface):
    """Draw the back left right surface."""
    #             1111
    #   01234567890123
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
    # 11
    # 12           |\
    # 13           ||
    # 14           ||
    # 15           ||
    # 16           ||
    # 17           ||
    # 18           |/
    surface.drawText(x=11, y=12, text="|\\")

    for y in range(13, 18):
        surface.drawText(x=11, y=y, text="||")

    surface.drawText(x=11, y=18, text="|/")

def drawBackCenterFrontSurface(surface):
    """Draw the back center front surface."""
    #             1111111111222
    #   01234567890123456789012
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
    # 11            ___________
    # 12           |           |
    # 13           |           |
    # 14           |           |
    # 15           |           |
    # 16           |           |
    # 17           |           |
    # 18           |___________|
    surface.drawText(x=12, y=11, text="___________")

    for y in range(12, 18):
        surface.drawText(x=11, y=y, text="|           |")

    surface.drawText(x=11, y=18, text="|___________|")

def drawBackRightLeftSurface(surface):
    """Draw the back right left surface."""
    #             11111111112222
    #   012345678901234567890123
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
    # 11
    # 12                      /|
    # 13                      ||
    # 14                      ||
    # 15                      ||
    # 16                      ||
    # 17                      ||
    # 18                      \|
    surface.drawText(x=22, y=12, text="/|")

    for y in range(13, 18):
        surface.drawText(x=22, y=y, text="||")

    surface.drawText(x=22, y=18, text="\\|")

def drawBackRightFrontSurface(surface):
    """Draw the back right front surface."""
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
    # 11                        ___________
    # 12                       |
    # 13                       |
    # 14                       |
    # 15                       |
    # 16                       |
    # 17                       |
    # 18                       |___________
    surface.drawText(x=24, y=11, text="___________")

    for y in range(12, 18):
        surface.plot(x=23, y=y, ch="|")

    surface.drawText(x=23, y=18, text="|___________")

def drawCenterLeftRightSurface(surface):
    """Draw the center left right surface."""
    #             11
    #   012345678901
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
    # 10         |\
    # 11         | \
    # 12         | |
    # 13         | |
    # 14         | |
    # 15         | |
    # 16         | |
    # 17         | |
    # 18         | |
    # 19         | /
    # 20         |/
    surface.drawText(x=9, y=10, text="|\\")
    surface.drawText(x=9, y=11, text="| \\")

    for y in range(12, 19):
        surface.drawText(x=9, y=y, text="| |")

    surface.drawText(x=9, y=19, text="| /")
    surface.drawText(x=9, y=20, text="|/")

def drawCenterLeftFrontSurface(surface):
    """Draw the center left front surface."""
    #
    #   0123456789
    #  0
    #  1
    #  2
    #  3
    #  4
    #  5
    #  6
    #  7
    #  8
    #  9_________
    # 10         |
    # 11         |
    # 12         |
    # 13         |
    # 14         |
    # 15         |
    # 16         |
    # 17         |
    # 18         |
    # 19         |
    # 20_________|
    surface.drawText(x=0, y=9, text="_________")

    for y in range(10, 20):
        surface.drawText(x=0, y=y, text="         |")

    surface.drawText(x=0, y=20, text="_________|")

def drawCenterCenterFrontSurface(surface):
    """Draw the center center front surface."""
    #             1111111111222222
    #   01234567890123456789012345
    #  0
    #  1
    #  2
    #  3
    #  4
    #  5
    #  6
    #  7
    #  8
    #  9          _______________
    # 10         |               |
    # 11         |               |
    # 12         |               |
    # 13         |               |
    # 14         |               |
    # 15         |               |
    # 16         |               |
    # 17         |               |
    # 18         |               |
    # 19         |               |
    # 20         |_______________|
    surface.drawText(x=10, y=9, text="_______________")

    for y in range(10, 20):
        surface.drawText(x=9, y=y, text="|               |")

    surface.drawText(x=9, y=20, text="|_______________|")

def drawCenterRightFrontSurface(surface):
    """Draw the center right front surface."""
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
    #  9                          _________
    # 10                         |
    # 11                         |
    # 12                         |
    # 13                         |
    # 14                         |
    # 15                         |
    # 16                         |
    # 17                         |
    # 18                         |
    # 19                         |
    # 20                         |_________
    surface.drawText(x=26, y=9, text="_________")

    for y in range(10, 20):
        surface.drawText(x=25, y=y, text="|         ")

    surface.drawText(x=25, y=20, text="|_________")

def drawCenterRightLeftSurface(surface):
    """Draw the center right left surface."""
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
    # 10                        /|
    # 11                       / |
    # 12                       | |
    # 13                       | |
    # 14                       | |
    # 15                       | |
    # 16                       | |
    # 17                       | |
    # 18                       | |
    # 19                       \ |
    # 20                        \|
    surface.drawText(x=24, y=10, text="/|")
    surface.drawText(x=23, y=11, text="/ |")

    for y in range(12, 19):
        surface.drawText(x=23, y=y, text="| |")

    surface.drawText(x=23, y=19, text="\\ |")
    surface.drawText(x=24, y=20, text="\\|")

def drawFrontLeftFrontSurface(surface):
    """Draw the front left front surface."""
    #             1111111111222222222233333
    #   01234567890123456789012345678901234
    #  0
    #  1
    #  2
    #  3
    #  4
    #  5_____
    #  6     |
    #  7     |
    #  8     |
    #  9     |
    # 10     |
    # 11     |
    # 12     |
    # 13     |
    # 14     |
    # 15     |
    # 16     |
    # 17     |
    # 18     |
    # 19     |
    # 20     |
    # 21     |
    # 22     |
    # 23     |
    # 24_____|
    surface.drawText(x=0, y=5, text="_____")

    for y in range(6, 24):
        surface.drawText(x=0, y=y, text="     |")

    surface.drawText(x=0, y=24, text="_____|")

def drawFrontLeftRightSurface(surface):
    """Draw the front left right surface."""
    #             1111111111222222222233333
    #   01234567890123456789012345678901234
    #  0
    #  1
    #  2
    #  3
    #  4
    #  5
    #  6     |\
    #  7     | \
    #  8     |  \
    #  9     |   \
    # 10     |   |
    # 11     |   |
    # 12     |   |
    # 13     |   |
    # 14     |   |
    # 15     |   |
    # 16     |   |
    # 17     |   |
    # 18     |   |
    # 19     |   |
    # 20     |   |
    # 21     |   /
    # 22     |  /
    # 23     | /
    # 24     |/
    surface.drawText(x=5, y=6, text="|\\")
    surface.drawText(x=5, y=7, text="| \\")
    surface.drawText(x=5, y=8, text="|  \\")
    surface.drawText(x=5, y=9, text="|   \\")

    for y in range(10, 21):
        surface.drawText(x=5, y=y, text="|   |")

    surface.drawText(x=5, y=21, text="|   /")
    surface.drawText(x=5, y=22, text="|  /")
    surface.drawText(x=5, y=23, text="| /")
    surface.drawText(x=5, y=24, text="|/")

def drawFrontCenterFrontSurface(surface):
    """Draw the front center front surface."""
    #             1111111111222222222233333
    #   01234567890123456789012345678901234
    #  0
    #  1
    #  2
    #  3
    #  4
    #  5      _______________________
    #  6     |                       |
    #  7     |                       |
    #  8     |                       |
    #  9     |                       |
    # 10     |                       |
    # 11     |                       |
    # 12     |                       |
    # 13     |                       |
    # 14     |                       |
    # 15     |                       |
    # 16     |                       |
    # 17     |                       |
    # 18     |                       |
    # 19     |                       |
    # 20     |                       |
    # 21     |                       |
    # 22     |                       |
    # 23     |                       |
    # 24     |_______________________|
    surface.drawText(x=6, y=5, text="_______________________")

    for y in range(6, 24):
        surface.drawText(x=5, y=y, text="|                       |")

    surface.drawText(x=5, y=24, text="|_______________________|")

def drawFrontRightFrontSurface(surface):
    """Draw the front right front surface."""
    #             1111111111222222222233333
    #   01234567890123456789012345678901234
    #  0
    #  1
    #  2
    #  3
    #  4
    #  5                              _____
    #  6                             |
    #  7                             |
    #  8                             |
    #  9                             |
    # 10                             |
    # 11                             |
    # 12                             |
    # 13                             |
    # 14                             |
    # 15                             |
    # 16                             |
    # 17                             |
    # 18                             |
    # 19                             |
    # 20                             |
    # 21                             |
    # 22                             |
    # 23                             |
    # 24                             |_____
    surface.drawText(x=30, y=5, text="_____")

    for y in range(6, 24):
        surface.drawText(x=29, y=y, text="|     ")

    surface.drawText(x=29, y=24, text="|_____")

def drawFrontRightLeftSurface(surface):
    """Draw the front right left surface."""
    #             1111111111222222222233333
    #   01234567890123456789012345678901234
    #  0
    #  1
    #  2
    #  3
    #  4
    #  5
    #  6                            /|
    #  7                           / |
    #  8                          /  |
    #  9                         /   |
    # 10                         |   |
    # 11                         |   |
    # 12                         |   |
    # 13                         |   |
    # 14                         |   |
    # 15                         |   |
    # 16                         |   |
    # 17                         |   |
    # 18                         |   |
    # 19                         |   |
    # 20                         |   |
    # 21                         \   |
    # 22                          \  |
    # 23                           \ |
    # 24                            \|
    surface.drawText(x=28, y=6, text="/|")
    surface.drawText(x=27, y=7, text="/ |")
    surface.drawText(x=26, y=8, text="/  |")
    surface.drawText(x=25, y=9, text="/   |")

    for y in range(10, 21):
        surface.drawText(x=25, y=y, text="|   |")

    surface.drawText(x=25, y=21, text="\\   |")
    surface.drawText(x=26, y=22, text="\\  |")
    surface.drawText(x=27, y=23, text="\\ |")
    surface.drawText(x=28, y=24, text="\\|")

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

def drawAdjacentLeftRightSurface(surface):
    """Draw the adjacent left right surface."""
    #   012345
    #  0\
    #  1 \
    #  2  \
    #  3   \
    #  4    \
    #  5     \
    #  6     |
    #  7     |
    #  8     |
    #  9     |
    # 10     |
    # 11     |
    # 12     |
    # 13     |
    # 14     |
    # 15     |
    # 16     |
    # 17     |
    # 18     |
    # 19     |
    # 20     |
    # 21     |
    # 22     |
    # 23     |
    # 24     |
    # 25     /
    # 26    /
    # 27   /
    # 28  /
    # 29 /
    # 30/
    surface.drawText(x=0, y=0, text="\\")
    surface.drawText(x=1, y=1, text="\\")
    surface.drawText(x=2, y=2, text="\\")
    surface.drawText(x=3, y=3, text="\\")
    surface.drawText(x=4, y=4, text="\\")
    surface.drawText(x=0, y=5, text="     \\")

    for y in range(6, 25):
        surface.drawText(x=0, y=y, text="     |")

    surface.drawText(x=5, y=25, text="/")
    surface.drawText(x=4, y=26, text="/")
    surface.drawText(x=3, y=27, text="/")
    surface.drawText(x=2, y=28, text="/")
    surface.drawText(x=1, y=29, text="/")
    surface.drawText(x=0, y=30, text="/")

def drawAdjacentRightLeftSurface(surface):
    """Draw the adjacent right left surface."""
    #             1111111111222222222233333
    #   01234567890123456789012345678901234
    #  0                                  /
    #  1                                 /
    #  2                                /
    #  3                               /
    #  4                              /
    #  5                             /
    #  6                             |
    #  7                             |
    #  8                             |
    #  9                             |
    # 10                             |
    # 11                             |
    # 12                             |
    # 13                             |
    # 14                             |
    # 15                             |
    # 16                             |
    # 17                             |
    # 18                             |
    # 19                             |
    # 20                             |
    # 21                             |
    # 22                             |
    # 23                             |
    # 24                             |
    # 25                             \
    # 26                              \
    # 27                               \
    # 28                                \
    # 29                                 \
    # 30                                  \
    surface.drawText(x=34, y=0, text="/")
    surface.drawText(x=33, y=1, text="/")
    surface.drawText(x=32, y=2, text="/")
    surface.drawText(x=31, y=3, text="/")
    surface.drawText(x=30, y=4, text="/")
    surface.drawText(x=29, y=5, text="/     ")

    for y in range(6, 25):
        surface.drawText(x=29, y=y, text="|     ")

    surface.drawText(x=29, y=25, text="\\")
    surface.drawText(x=30, y=26, text="\\")
    surface.drawText(x=31, y=27, text="\\")
    surface.drawText(x=32, y=28, text="\\")
    surface.drawText(x=33, y=29, text="\\")
    surface.drawText(x=34, y=30, text="\\")

def drawViewableArea(surface, viewableArea):
    """Create the viewable area surface."""
    if not isinstance(surface, Surface) or not isinstance(viewableArea, list):
        raise TypeError

    if len(viewableArea) != VIEWABLE_AREA_HEIGHT or len(viewableArea[0]) != VIEWABLE_AREA_WIDTH:
        raise ValueError(f"Viewable area must be {VIEWABLE_AREA_HEIGHT}x{VIEWABLE_AREA_WIDTH}")

    dumpViewableArea(viewableArea)

    # Back Row
    if viewableArea[0][0] == Map.TILE_OUTSIDE_MAP:
        drawBackLeftFrontSurface(surface=surface)
        if viewableArea[0][1] != Map.TILE_OUTSIDE_MAP:
            drawBackLeftRightSurface(surface=surface)

    if viewableArea[0][1] == Map.TILE_OUTSIDE_MAP:
        drawBackCenterFrontSurface(surface=surface)

    if viewableArea[0][2] == Map.TILE_OUTSIDE_MAP:
        drawBackRightFrontSurface(surface=surface)
        if viewableArea[0][1] != Map.TILE_OUTSIDE_MAP:
            drawBackRightLeftSurface(surface=surface)

    # Center Row
    if viewableArea[1][0] == Map.TILE_OUTSIDE_MAP:
        drawCenterLeftFrontSurface(surface=surface)
        if viewableArea[1][1] != Map.TILE_OUTSIDE_MAP:
            drawCenterLeftRightSurface(surface=surface)

    if viewableArea[1][1] == Map.TILE_OUTSIDE_MAP:
        drawCenterCenterFrontSurface(surface=surface)

    if viewableArea[1][2] == Map.TILE_OUTSIDE_MAP:
        drawCenterRightFrontSurface(surface=surface)
        if viewableArea[1][1] != Map.TILE_OUTSIDE_MAP:
            drawCenterRightLeftSurface(surface=surface)

    # Front Row
    if viewableArea[2][0] == Map.TILE_OUTSIDE_MAP:
        drawFrontLeftFrontSurface(surface=surface)
        if viewableArea[2][1] != Map.TILE_OUTSIDE_MAP:
            drawFrontLeftRightSurface(surface=surface)

    if viewableArea[2][1] == Map.TILE_OUTSIDE_MAP:
        drawFrontCenterFrontSurface(surface=surface)

    if viewableArea[2][2] == Map.TILE_OUTSIDE_MAP:
        drawFrontRightFrontSurface(surface=surface)
        if viewableArea[2][1] != Map.TILE_OUTSIDE_MAP:
            drawFrontRightLeftSurface(surface=surface)

    if viewableArea[3][0] == Map.TILE_OUTSIDE_MAP:
        drawAdjacentLeftRightSurface(surface=surface)

    if viewableArea[3][2] == Map.TILE_OUTSIDE_MAP:
        drawAdjacentRightLeftSurface(surface=surface)
