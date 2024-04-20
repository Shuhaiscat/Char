import pygame as pg

pg.mixer.init()

size = (500, 500)
screen = pg.display.set_mode(size)

fps = 35
clock = pg.time.Clock()

backgr = pg.image.load("backgr.png")

backgr = pg.transform.scale(backgr, size)

charster = pg.image.load("Character.png")

charster = pg.transform.scale(charster, (300, 400))

character_rect = charster.get_rect(center=(size[0] // 2, size[1] // 2))
small_rect = charster.get_rect(center=(size[0] // 2, size[1] // 2))

#pg.mixer.music.load("music.mp3")
#pg.mixer.music.play()

while True:

    for event in pg.event.get():
        if event == pg.QUIT:
            quit()
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(event.pos)
                character_rect.center = event.pos

    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT]:
        charster.x -= 5
    if keys[pg.K_RIGHT]:
        charster.x += 5

mouse_pos = pg.mouse.get_pos()
mouse_keys = pg.mouse.get_pressed()

if mouse_keys[0]:
    charster.center = mouse_pos


screen.fill(pg.Color(34, 255, 21))

screen.blit(backgr, (0, 0))
screen.blit(charster, character_rect)

pg.draw.rect(screen, pg.Color("red"), small_rect)

pg.display.flip()
clock.tick(fps)
