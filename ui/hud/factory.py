"""Factory to create the HUD surface."""

from ..surface import Surface
from ..viewPort import factory as viewPortFactory

def create(viewableArea, messages=[]):
    """Create the HUD surface."""
    hud = Surface(width=128, height=34, initChar=None)

    viewPort = viewPortFactory.create(viewableArea)

    # Draw the view port on the HUD
    viewPort.drawToSurface(hud)

    # Write out any messages
    y = 0

    for message in messages:
        hud.drawText(45, y, message)
        y += 1

    return hud
