"""Define the Viewport Border Surface."""

from ..surface import Surface

width = 43
height = 34

border = Surface(width=width, height=height, initChar=None)

horizontalBorder = "[<+>]==============[<:>]==============[<+>]"
verticalBorder = "| |"

border.drawText(x=0, y=0, text=horizontalBorder)
border.drawText(x=0, y=height - 1, text=horizontalBorder)

for y in range(1, height - 1):
    border.drawText(x=1, y=y, text=verticalBorder)
    border.drawText(x=width - 4, y=y, text=verticalBorder)
