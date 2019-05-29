"""Define the Viewport Border Surface."""

from .surface import Surface

width = 6
height = 30

#             11111111112222222222233333
#   012345678901234567890123456789012345
#  0|\                                /|
#  1| \                              / |
#  2|  \                            /  |
#  3|   \                          /   |
#  4|    \                        /    |
#  5|     \                      /     |
#  6|     |\                     |     |
#  7|     | \                    |     |
#  8|     |  \                   |     |
#  9|     |   \               ___|     |
# 10|     |   |\            /|   |     |
# 11|     |   | |          | |   |     |
# 12|     |   | |          | |   |     |
# 13|     |   | |          | |   |     |
# 14|     |   | |          | |   |     |
# 15|     |   | |          | |   |     |
# 16|     |   | |          | |   |     |
# 17|     |   | |          | |   |     |
# 18|     |   | /          \ |   |     |
# 19|     |   |/            \|___|     |
# 20|     |   /                  |     |
# 21|     |  /                   |     |
# 22|     | /                    |     |
# 23|     |/                     |     |
# 24|     /                      \     |
# 25|    /                        \    |
# 26|   /                          \   |
# 27|  /                            \  |
# 28| /                              \ |
# 29|/                                \|
viewPortBackLeftClosed = Surface(width, height, initChar=None)

for x in range(0, 6):
    print(x)
    viewPortBackLeftClosed.plot(x, x, "\\")

for y in reversed(range(24, 30)):
    viewPortBackLeftClosed.plot(30 - y - 1, y, "/")
