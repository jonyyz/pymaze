"""Define the Viewport Border Surface."""

from ..surface import Surface

width = 43
height = 34

border = Surface(width=width, height=height, initChar=None)

horizontalBorder = "[<+>]==============[<:>]==============[<+>]"
verticalBorder = "| |"

border.drawText(0, 0, horizontalBorder)
border.drawText(0, height - 1, horizontalBorder)

for y in range(1, height - 1):
    border.drawText(1, y, verticalBorder)
    border.drawText(width - 4, y, verticalBorder)
