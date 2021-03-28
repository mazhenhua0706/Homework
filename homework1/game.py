from homework1.hero_factory import HeroFactory

hero_factory = HeroFactory()
timo = hero_factory.create_hero("timo")
police = hero_factory.create_hero("police")

timo.speak_lines()
timo.fight(police.hp, police.power)
police.speak_lines()
police.fight(timo.hp, timo.power)