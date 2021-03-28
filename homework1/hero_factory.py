from timo import Timo
from police import Police


class HeroFactory:
    def create_hero(self, name):
        if name == "timo":
            return Timo()
        elif name == "police":
            return Police()
        else:
            raise Exception(f"{name}英雄不在英雄工厂中")
