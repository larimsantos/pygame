import pygame
# iniciando as funçoes basicas da biblioteca
pygame.init()
# para fechar o jogo, usar "pygame.quit()"

# criando a classe "Window" de janelas
class Window:
    '''
    atributos:
    '''
    __width = 0 #largura
    __height = 0 #altura
    __color = (255, 255, 255) #cor

    def __init__(self, largura, altura): #construtor
        self.__width = largura
        self.__height = altura

    def returnWinSize(self): #retorna o tamanho da tela
        return (self.__width, self.__height)
    
    def returnColor(self): #retorna a cor da janela
        return (self.__color)
# terminamos de criar a classe "Window"

#iniciando a construção da janela do pygame
w = Window(500, 500) #cria um objeto janela com dimensões 500x500
testwindow = pygame.display.set_mode(w.returnWinSize()) #inicializa a janela
######

pygame.display.set_caption("Teste Pygame") # alterar o nome da janela

#Alterar a cor de fundo da janela "testwindow":
testwindow.fill(w.returnColor()) 
######

#text:#
pygame.font.init()
font = pygame.font.Font('squaremaze.ttf', 40) #fonte#
testtext = font.render("hello world", True, (242, 133, 138)) #(configuraçao)rendaçao do texto#
textRect = testtext.get_rect() #getting o texto#
textRect.center = ((250), (250)) #posicionando o texto no centro#
testwindow.blit(testtext, textRect)
#######

#drawin our border lines:#
linhaVerticalEsquerda = pygame.draw.line(testwindow, (132, 165, 184), (1,0), (1,500), 9)#desenhando uma linha (vertical esquerdo)#
linhaVerticalDireita = pygame.draw.line(testwindow, (132, 165, 184), (498,0), (498,500), 9)#desenhando uma linha (vertical direito)#
linhaHorizontalSuperior = pygame.draw.line(testwindow, (132, 165, 184), (1,1), (498,1), 9)#desenhando uma linha (horizontal superior)#
linhaHorizontalInferior = pygame.draw.line(testwindow, (132, 165, 184), (0,498), (498,498), 9)#desenhando uma linha (horizontal inferior)#
#########

#drawin our poligon:#
pygame.draw.polygon(testwindow, (179,218,241), ((18,68), (482,68), (482,18), (18,18)), 0)
# # # # #

#"exibindo" o texto na janela:#
testwindow.blit(testtext, textRect)

#atualizando a janela:#
pygame.display.update()
#########
nClicks = -1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("clicked")
          