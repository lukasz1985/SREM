import pygame

import assets
import player
import tests
import iso
import gui
import world
import interface


# The main game class that is intantiated on startup.
class Game:

    def __init__(self):
        pygame.init()
        self.window = None  # The pygame window Surface
        self.input = None
        self.view = None
        self.gui = None
        self.test = None
        self.done = False  # A flag for the game loop indicating if the game is done playing.
        self.player = None
        self.world = None
        self.interface = None

    def run(self):
        self.window = pygame.display.set_mode((600, 800), pygame.RESIZABLE)
        pygame.display.set_caption("SREM")
        pygame.display.set_icon(assets.load_image("assets/icon.png"))

        self.view = iso.View(self.window)
        self.gui = gui.Gui()

        self.onInit()

        self.test = tests.TestIso(self)
        if self.test is not None:
            self.test.onInit()

        clock = pygame.time.Clock()

        while not self.done:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                else:
                    self.gui.on_event(event)

            self.update(clock)
            self.draw()

            pygame.display.flip()
            clock.tick(60)

    def update(self, clock):
        self.world.update(clock)
        self.interface.update(clock)

    def draw(self):
        self.window.fill((0, 0, 0))
        self.view.draw()
        self.gui.draw(self.window)

    def onInit(self):
        self.player = player.Player(self)
        self.world = world.World(self)
        self.interface = interface.Interface(self)
        self.world.create()
        self.interface.display()
        pass


if __name__ == "__main__":
    game = Game()
    game.run()
