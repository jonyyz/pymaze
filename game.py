"""Defines the main game object."""


from map import Map
from player import Player
from direction import Direction


class Game:
    """The main game object."""
    def __init__(self, mapName, playerName):
        self.__map = Map(mapName)
        self.__player = Player(playerName, self.__map.startLocation)

    def start(self):
        """Start the game loop."""
        self.prompt(extraLine=False)

    def render(self, message=None, extraLine=True):
        """Render the current state of the game."""
        if message is not None:
            print(message)

    def prompt(self, extraLine=True):
        """Prompt for input."""
        if extraLine is True:
            print()

        self.render()
        self.processInput(input("> ").strip())

    def processInput(self, inputText):
        """Process input text."""
        if len(inputText) > 0:
            command = inputText.lower()

            if command == "quit":
                print("I am here!")
                return
            elif command == "help":
                self.displayHelp()
            elif command == "look":
                print(f"You are facing {Direction.getName(self.__player.facingDirection)}.")
                print(f"Your location is: {self.__player.location}")
                self.render()
            elif command == "move":
                self.movePlayer()
            elif command == "left":
                self.__player.turnLeft()
                print(f"You are now facing {Direction.getName(self.__player.facingDirection)}.")
            elif command == "right":
                self.__player.turnRight()
                print(f"You are now facing {Direction.getName(self.__player.facingDirection)}.")
            else:
                print(f"I'm sorry I don't understand the command: {inputText}.  Try 'help' if you need help")

        self.prompt()

    def displayHelp(self):
        """Display the help."""
        print("""Python Maze Game
----------------
help    - Display the commands you can use
quit    - Quit the game

look    - Look at the current room
move    - Move in the direction the player is facing
left    - Turn left
right   - Turn right""")

    def movePlayer(self):
        """Attempt to move the player."""
        destination = self.__map.getDestinationInDirectionFromLocation(
            self.__player.location,
            self.__player.facingDirection
        )

        if destination is None:
            print("There's a wall in your way!")
        else:
            print(f"You walk {Direction.getName(self.__player.facingDirection)}.")
            self.__player.location = destination
