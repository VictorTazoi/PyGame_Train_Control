import pygame as pg

pg.init()

tela = pg.display.set_mode((800,600))

#Carregar a imagem
nave = pg.image.load("nave.png")
space = pg.image.load("space.jpeg")
xnave = 0
ynave = 0

while True:
    # Procurar por eventos
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            
        #Move o personagem com as teclas do teclado
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_RIGHT:
                xnave += 1
            elif e.key == pg.K_LEFT:
                xnave -= 1
            elif e.key == pg.K_UP:
                ynave -= 1
            elif e.key == pg.K_DOWN:
                ynave += 1
            
    tela.fill((255, 255, 255))
    
    #Desenhar o fundo
    tela.blit(space, (0, 0))
    
    #Desenhar a imagem na tela
    tela.blit(nave, (xnave, ynave)) #Define a variavel da imagem. O redimensionamento deve ser feito no tratamento externo da imagem
    
    pg.display.flip()