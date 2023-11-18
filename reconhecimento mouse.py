import pygame as pg

pg.init()


tela = pg.display.set_mode((600, 400))

pg.mouse.set_visible(False)

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
    
    esquerdo, meio, direito = pg.mouse.get_pressed()
    
    xmouse, ymouse = pg.mouse.get_pos()
    
    if esquerdo:
        cor = (255, 0, 0)
    elif direito:
        cor = (255, 255, 0)
    elif meio:
        cor = (0, 255, 255)
    else:
        cor = (0, 0, 255)
    
    tela.fill((255, 255, 255))
    
    pg.draw.circle(tela, cor, (xmouse, ymouse), 15)
    
    pg.display.flip()