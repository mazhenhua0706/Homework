from timo import Timo
from police import Police


class HeroFactory:
    def create_hero(self, name):
        if name == "timo":
            return Timo()
        elif name == "police":
            return Police()
        else:
            raise Exception("此英雄不再英雄工厂中")


hero_factory = HeroFactory()
timo = hero_factory.create_hero("timo")
police = hero_factory.create_hero("police")

timo.speak_lines()
timo.fight(police.hp, police.power)
police.speak_lines()
police.fight(timo.hp, timo.power)