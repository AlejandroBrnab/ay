class Pokemon:
    def __init__(self, name, power, hp, defense, attack):
        self.name = name
        self.power = power
        self.hp = hp
        self.defense = defense
        self.attack = attack

    def show_everything(self):
        print(self.name, self.power, self.hp, self.defense, self.attack)



pikachu = Pokemon("Pikachu", 800, 700, 800, 800)
charmander = Pokemon("Charmander", 700, 780, 700, 900)
jigglypuff = Pokemon("Jigglypuff", 800, 900, 1000, 800)

jigglypuff.show_everything()