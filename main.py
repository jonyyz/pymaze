"""Main entry point for application."""

# Copyright (C) 2019 Jon Cameron.  All Rights Reserved.

from game import Game

def main():
    """Start maze game."""
    game = Game("test", "El Conquistador")
    game.start()


if __name__ == '__main__':
    main()
