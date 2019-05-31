"""Defines the main game object."""

import os
import platform

from map import Map
from player import Player
from direction import Direction

import ui.hud.factory as HUDFactory

class Game:
    """The main game object."""

    def __init__(self, mapName, playerName):
        self.__map = Map(mapName)
        self.__player = Player(playerName, self.__map.startLocation)
        self.__messages = []
        self.__renderHUD = False
        self.__quit = False

    def __clearScreen():
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    def start(self):
        """Start the game loop."""
        firstTime = True
        self.render(renderHUD=True)

        while not self.__quit:
            self.prompt(extraLine=not firstTime)
            firstTime = False

    def writeMessage(self, text):
        """Queue a message to be written to the screen."""
        self.__messages.append(text)

    def getPlayerViewableArea(self):
        """Get the player's viewable area."""
        return self.__map.getViewableArea(
            originLocation=self.__player.location,
            direction=self.__player.facingDirection
        )

    def render(self, renderHUD=False):
        """Render the current state of the game."""
        if renderHUD:
            Game.__clearScreen()

            print(f"You are facing {self.__player.facingDirectionName}.")
            print(f"Your location is: {self.__player.location}")

            hud = HUDFactory.create(
                viewableArea=self.getPlayerViewableArea(),
                messages=self.__messages
            )
            hud.render()
        else:
            if len(self.__messages) > 0:
                for message in self.__messages:
                    print(message)

        self.__messages.clear()

    def prompt(self, extraLine=True):
        """Prompt for input."""
        if extraLine is True:
            print()

        if self.__renderHUD:
            self.render()
            self.__renderHUD = False

        self.processInput(input("> ").strip())

    def processInput(self, inputText):
        """Process input text."""
        if len(inputText) > 0:
            command = inputText.lower()

            renderHUD = False

            if command == "quit":
                self.__quit = True
            elif command == "help":
                self.displayHelp()
            elif command == "look":
                renderHUD = True
            elif command == "forward" or command == "f":
                self.movePlayerForward()
                renderHUD = True
            elif command == "back" or command == "b":
                self.movePlayerBackward()
                renderHUD = True
            elif command == "left" or command == "l":
                self.__player.turnLeft()
                renderHUD = True
            elif command == "right" or command == "r":
                self.__player.turnRight()
                renderHUD = True
            else:
                self.writeMessage(
                    text=f"I'm sorry I don't understand the command: {inputText}.  Try 'help' if you need help"
                )

            self.render(renderHUD=renderHUD)

    def displayHelp(self):
        """Display the help."""
        print("""Python Maze Game
----------------
help       - Display the commands you can use
quit       - Quit the game

look       - Look at the current room
forward, f - Move in the direction the player is facing
back, b    - Move in the direction opposite of the one the player is facing
left, l    - Turn left
right, r   - Turn right""")

    def movePlayerForward(self):
        """Attempt to move the player forward."""
        self.movePlayer(direction=self.__player.facingDirection)

    def movePlayerBackward(self):
        """Attempt to move the player backward."""
        direction = Direction.getOppositeDirection(direction=self.__player.facingDirection)

        self.movePlayer(direction=direction)

    def movePlayer(self, direction):
        """Attempt to move the player to the destination."""
        destination = self.__map.getDestinationInDirectionFromLocation(
            originLocation=self.__player.location,
            direction=direction
        )

        if destination is None:
            self.writeMessage(text="There's a wall in your way!")
        else:
            self.writeMessage(text=f"You walk {Direction.getName(value=direction)}.")
            self.__player.location = destination
