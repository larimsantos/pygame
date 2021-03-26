#implementando uma classe "Pokemon"#
class Pokemon:
    '''
    properties:

    name (nome do pokémon)
    hp (quantidade de vida do pokémon)
    level (o nível do pokémon)
    element (o elemento ao qual o pokémon pertence)
    '''
    def __init__(self, nome, hp, level, elemento):
        self._nome = nome 
        self._hp = hp 
        self._level = level 
        self._elemento = elemento 

    
    def pokemon_nome(self):
        return self._nome
        
    @property
    def pokemon_hp(self):
        return self._hp

    @property
    def pokemon_level(self):
        return self._level
        
    @property
    def pokemon_elemento(self):
        return self._elemento
########

Charizard = Pokemon("Charizard", 78, 100, "fire")
Bulbassauro = Pokemon("Bulbassauro", 45, 100, "grass")
Blastoise = Pokemon("Blastoise", 79, 100, "water")
Arcanine = Pokemon("Arcanine", 90, 100, "fire")
Dragonite = Pokemon("Dragonite", 91, 100, "dragon,flying")
Scyther = Pokemon("Scyther", 70, 100, "bug, flying")
Pikachu = Pokemon("Pikachu", 35, 100, "eletric")
Mewtwo = Pokemon("Mewtwo", 106, 100, "psychic")
Mew = Pokemon("Mew", 100, 100, "psychic")
Kabutops = Pokemon("Kabutops", 60, 100, "rock, water")

pokémons = [Charizard, Bulbassauro, Blastoise, Arcanine, Dragonite, Scyther, Pikachu, Mewtwo, Mew, Kabutops]
Mew.pokemon_hp