"""Defines the surface object."""

class Surface:
    """A surface to render."""

    def __init__(self, width, height, initChar=chr(32)):
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError
        if width <= 0 or height <= 0:
            raise ValueError

        self.__width = width
        self.__height = height
        self.__surface = [[initChar for x in range(width)] for y in range(height)]

    def __str__(self):
        return self.render()

    @property
    def width(self):
        """Get the width of the surface."""
        return self.__width

    @property
    def height(self):
        """Get the height of the surface."""
        return self.__height

    def __checkCoordinatesInBounds(self, x, y):
        """Check coordinates to ensure they are within the surface bounds."""
        if x < 0 or y < 0 or x > self.__width - 1 or y > self.__height - 1:
            raise ValueError(f"X={x},Y={y},width={self.__width},height={self.__height}")

        return (x, y)

    def plot(self, x, y, ch):
        """Draw a character on the surface at the specified coordinates."""
        if not isinstance(x, int) or not isinstance(y, int) or not isinstance(ch, str):
            raise TypeError

        x, y = self.__checkCoordinatesInBounds(x=x, y=y)

        if len(ch) == 0:
            raise ValueError

        self.__surface[y][x] = ch[0]

    def drawText(self, x, y, text, horizontal=True):
        """Draw text on the surface at the specified coordinates."""
        if not isinstance(x, int) or not isinstance(y, int) or not isinstance(text, str):
            raise TypeError

        x, y = self.__checkCoordinatesInBounds(x=x, y=y)

        if len(text) == 0:
            # Nothing to draw
            return

        for ch in text:
            self.plot(x=x, y=y, ch=ch)
            if horizontal:
                x += 1
            else:
                y += 1

    def render(self):
        """Render the surface."""
        # rowNumber = 0
        for row in self.__surface:
            # print(f"{rowNumber:<3}", end="")
            # rowNumber += 1

            for col in row:
                print(chr(32) if col is None else col, end="")

            print()

    def drawToSurface(self, toSurface, x=0, y=0):
        """Draw a surface into this surface at the specified coordinates."""
        if not isinstance(x, int) or not isinstance(y, int) or not isinstance(toSurface, Surface):
            raise TypeError

        drawToX, drawToY = toSurface.__checkCoordinatesInBounds(x=x, y=y)

        if drawToX + self.__width > toSurface.width or drawToY + self.__height > toSurface.height:
            raise TypeError(f"The surface to draw is too big to fit into the destination surface at X={x},Y={y}")

        for sourceY in range(0, self.__height):
            for sourceX in range(0, self.__width):
                ch = self.__surface[sourceY][sourceX]
                if ch is not None:
                    toSurface.plot(x=sourceX + drawToX, y=sourceY + drawToY, ch=ch)
