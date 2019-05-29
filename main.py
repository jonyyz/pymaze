"""Main entry point for application."""


from game import Game

def main():
    """Start maze game."""
    game = Game("test", "El Conquistador")
    game.start()


if __name__ == '__main__':
    main()
