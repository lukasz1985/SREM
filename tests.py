import iso
import assets
from main import Game
from vectors import vec3

class Test:

    # Abstract method that is run upon initialization of the test:
    def run(self):
        pass


class TestIso(Test):
    pass


class TestGame(Test):

    def run(self):
        game = Game(600, 800)
        game.init()
        game.loop()


class TestAbandonment(Test):

    def run(self):
        game = Game(600, 800)
        game.init()
        game.world.building.set_contentment(0)
        for _ in range(0,8):
            game.world.building.upgrade()
        game.loop()

class TestHelipad(Test):

    def run(self):
        game = Game(600,800)
        game.init()
        for _ in range(0,11):
            game.world.building.upgrade()
        game.world.building.make_helipad()
        game.loop()


if __name__ == "__main__":
    #test = TestAbandonment()
    test = TestHelipad()
    test.run()

