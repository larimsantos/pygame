#implementando uma classe "Window" para janelas#
class Window:
    '''
    proprerties:
    height
    width
    color
    '''
    def __init__(self, height, width, color): #construtor#
        self.__height = height (int)
        self.__width = width (int)
        self.__wcolor = color (tuple)

    #geters e setters:#
    @property #retorna a altura#
    def get_height(self):
        return height
    
    @property #retorna a largura#
    def get_width(self):
        return width
    
    @property #retorna a cor#
    def get_wcolor(self):
        return wcolor
    
    @wcolor.setter #muda a cor#
    def wcolor(self, wcolor):
        self.wcolor = wcolor
########

#implementando a classe "Ataque"#
class Ataque:
    '''
    properties:
    
    nome do ataque
    taxa de letalidade (%)
    dano extra (bool)** (se sim, qual a taxa de dano extra - quanto dano a mais ele causaria?)
    '''
    def __init__(self, name, damage, edamage):
        self.__attack_name = name (str)
        self.__damage = damage (float)
        self.__edamage (bool)

    @property
    def get_attack_name(self):
        return self.__attack_name
    
    @property
    def get_damage(self):
        return self.__damage
    
    @property
    def get_edamage(self):
        return self.__edamage
        