
import pygame
import time
import math
key_collected = False
scissors_collected = False
food_collected = False
bovel_collected = False
seed_collected = False
wateringCan_collected = False
fens_collected = False
knife_collected = False
seed_used = False
wateringCan_used = False
fens_used = False
knife_used = False
radio = False
fens_blit = False
frame6 = 0
def showhint(txt):
    textpict = font.render(txt, True, (255,255,255))
    textpictrect = textpict.get_rect()
    textpictrect.y = 10
    textpictrect.x = 100
    screen.blit(textpict, textpictrect)
    pygame.display.flip()
    time.sleep(4)
def iscollide(x1,y1,x2,y2):
    a = x1 - x2
    b = y1 - y2
    a_sq = a*a
    b_sq = b*b
    c_sq = a_sq + b_sq
    c = math.sqrt(c_sq)
    if c <= 32:
        return True
    else:
        return False
def draw_hall(indoors2, indoors2_rect, indoors22, indoors2_rect2,indoors23,indoors2_rect3):
    global frame6
    frame6 += 1
    if frame6 <= 10:
        screen.blit(indoors2, indoors2_rect)
    elif frame6 <= 20:
        screen.blit(indoors22, indoors2_rect2)
    elif frame6 <= 30:
        screen.blit(indoors23, indoors2_rect3)
    else:
        screen.blit(indoors23, indoors2_rect3)
        frame6 = 0
def draw_bedroom(bedroom, bedroom_rect, key, key_rect, seed, seed_rect, bedroom2, bedroom2_rect, bedroom3, bedroom3_rect):
    global frame6
    frame6 += 1
    if frame6 <= 10:
        screen.blit(bedroom, bedroom_rect)
    elif frame6 <= 20:
        screen.blit(bedroom2, bedroom2_rect)
    elif frame6 <= 30:
        screen.blit(bedroom3, bedroom3_rect)
    else:
        screen.blit(bedroom3, bedroom3_rect)
        frame6 = 0
    if curmode == 4:
        if not seed_collected:
            screen.blit(seed, seed_rect)
    if curmode == 2:
        if not key_collected:
            screen.blit(key, key_rect)
def draw_kitchen(kitchen, kitchen_rect, frame5,kitchen2,kitchen_rect2,kitchen3,kitchen3_rect, bovel, bovel_rect, food, food_rect, knife, knife_rect, wateringCan, wateringCan_rect):
    global frame6
    frame6 += 1
    if frame6 <= 10:
        screen.blit(kitchen, kitchen_rect)
    elif frame6 <= 20:
        screen.blit(kitchen2, kitchen_rect2)
    elif frame6 <= 30:
        screen.blit(kitchen3, kitchen_rect3)
    else:
        screen.blit(kitchen3, kitchen_rect3)
        frame6 = 0
    screen.blit(bovel, bovel_rect)
    if curmode == 4:
        if not knife_collected:
            screen.blit(knife, knife_rect)
        if not wateringCan_collected:
            screen.blit(wateringCan, wateringCan_rect)
    if curmode == 2:
        if not food_collected:
            screen.blit(food, food_rect)
        if bovel_collected:
                frame5 += 1
                global x2
                global dx2
                x2 = x2 + dx2
                cat1_rect.x = x2
                cat2_rect.x = x2
                teapot_rect.x = x2 - 20
                teapot_rect.y = y2 - 20
                screen.blit(teapot,teapot_rect)
                if frame5 < 15:
                    screen.blit(cat1,cat1_rect)
                elif frame5 >= 15:
                    screen.blit(cat2,cat2_rect)
                if frame5 > 30:
                    frame5 = 0
                time.sleep(1/60)
def draw_bathroom(bathroom, bathroom_rect, bathroom2, bathroom_rect2, bathroom3, bathroom_rect3, scissors, scissors_rect, fens, fens_rect):
    global frame6
    frame6 += 1
    if frame6 <= 10:
        screen.blit(bathroom, bathroom_rect)
    elif frame6 <= 20:
        screen.blit(bathroom2, bathroom_rect2)
    elif frame6 <= 30:
        screen.blit(bathroom3, bathroom_rect3)
    else:
        screen.blit(bathroom3, bathroom_rect3)
        frame6 = 0
    if curmode == 2:
        if not scissors_collected:
            screen.blit(scissors, scissors_rect)
    if curmode == 4:
        if not fens_collected:
            screen.blit(fens, fens_rect)

def draw_outside(YotieHouse, YotieHouse_rect, YotieHouse2, YotieHouse_rect2, YotieHouse3, YotieHouse_rect3, pumpkin, pumpkin_rect, fens, fens_rect, pumpkin2, pumpkin2_rect):
    global frame6
    frame6 += 1
    if frame6 <= 10:
        screen.blit(YotieHouse, YotieHouse_rect)
    elif frame6 <= 20:
        screen.blit(YotieHouse2, YotieHouse_rect2)
    elif frame6 <= 30:
        screen.blit(YotieHouse3, YotieHouse_rect3)
    else:
        screen.blit(YotieHouse3, YotieHouse_rect3)
        frame6 = 0
    if curmode == 4 and seed_used == True:
        screen.blit(pumpkin, pumpkin_rect)
    if curmode == 4 and fens_used:
        fens_rect.x = 400
        screen.blit(pumpkin2, pumpkin2_rect)
        screen.blit(fens, fens_rect)

pygame.init()
screen = pygame.display.set_mode((640,480))
x = 220
y = 289
dy = 0
frame = 0
frame2 = 0
frame3 = 0
frame4 = 0
frame5 = 0
frame7 = 0
dx = 0
dl = 1
curmode = 1
black = (0,0,0)
yetil2 = pygame.image.load('pics/yetil2.png')
yetil2 = pygame.transform.scale(yetil2, (32, 32))
yetil2_rect =  yetil2.get_rect()
bovel = pygame.image.load('pics/bovel.png')
bovel = pygame.transform.scale(bovel, (32, 32))
bovel_rect =  bovel.get_rect()
bovel_rect.x = 140
bovel_rect.y = 293
key = pygame.image.load('pics/key.png')
key = pygame.transform.scale(key, (32, 32))
key_rect =  key.get_rect()
key_rect.x = 250
key_rect.y = 293
fens = pygame.image.load('pics/fens.png')
fens = pygame.transform.scale(fens, (32, 32))
fens_rect =  fens.get_rect()
fens_rect.x = 140
fens_rect.y = 293
seed = pygame.image.load('pics/seed.png')
seed = pygame.transform.scale(seed, (32, 32))
seed_rect =  seed.get_rect()
seed_rect.x = 250
seed_rect.y = 293
wateringCan = pygame.image.load('pics/wateringCan.png')
wateringCan = pygame.transform.scale(wateringCan, (32, 32))
wateringCan_rect =  wateringCan.get_rect()
wateringCan_rect.x = 190
wateringCan_rect.y = 293
knife = pygame.image.load('pics/knife.png')
knife = pygame.transform.scale(knife, (32, 32))
knife_rect =  knife.get_rect()
knife_rect.x = 250
knife_rect.y = 293
pumpkin = pygame.image.load('pics/pumpkin.png')
pumpkin = pygame.transform.scale(pumpkin, (32, 32))
pumpkin_rect =  pumpkin.get_rect()
pumpkin_rect.x = 400
pumpkin_rect.y = 293
pumpkin2 = pygame.image.load('pics/pumpkin2.png')
pumpkin2 = pygame.transform.scale(pumpkin2, (32, 32))
pumpkin2_rect =  pumpkin2.get_rect()
pumpkin2_rect.x = 400
pumpkin2_rect.y = 293
teapot = pygame.image.load('pics/teapot.png')
teapot = pygame.transform.scale(teapot, (32, 32))
teapot_rect =  teapot.get_rect()
scissors = pygame.image.load('pics/scissors.png')
scissors = pygame.transform.scale(scissors, (32, 32))
scissors_rect =  scissors.get_rect()
scissors_rect.x = 300
scissors_rect.y = 240
food = pygame.image.load('pics/food.png')
food = pygame.transform.scale(food, (32, 32))
food_rect =  food.get_rect()
food_rect.x = 300
food_rect.y = 250
yetil1 = pygame.image.load('pics/yetil1.png')
yetil1 = pygame.transform.scale(yetil1, (32, 32))
yetil1_rect =  yetil1.get_rect()
yetir1 = pygame.image.load('pics/yetir1.png')
yetir1 = pygame.transform.scale(yetir1, (32, 32))
yetir1_rect =  yetir1.get_rect()
yetir2 = pygame.image.load('pics/yetir2.png')
yetir2 = pygame.transform.scale(yetir2, (32, 32))
yetir2_rect =  yetir2.get_rect()
yeti_standing_l = pygame.image.load('pics/yeti_standing_l.png')
yeti_standing_l = pygame.transform.scale(yeti_standing_l, (32, 32))
yeti_standing_l_rect = yeti_standing_l.get_rect()
yeti_standing_r = pygame.image.load('pics/yeti_standing_r.png')
yeti_standing_r = pygame.transform.scale(yeti_standing_r, (32, 32))
yeti_standing_r_rect = yeti_standing_r.get_rect()
font = pygame.font.Font('freesansbold.ttf', 16)
text = font.render('На хеллоуин Йети сидел у себя дома', True, (255,255,255))
text2 = font.render('Не все знают, что Йети любит чайку попить...', True, (255,255,255))
text3 = font.render('Но вдруг в дверь постучали', True, (255,255,255))
text4 = font.render('тук', True, (255,255,255))
text5 = font.render('Йети открыл дверь и увидел детей которые орали:', True, (255,255,255))
text7 = font.render('сладость или гадость!', True, (255,255,255))
text6 = font.render('А где чайник?', True, (255,255,255))
text8 = font.render('Йети дал им конфетку и пошёл домой.', True, (255,255,255))
textwin = font.render('Чайник найден! Оказывается вором был кот(вы победили)', True, (255,255,255))
# create a rectangular object for the
# text surface object
text9 = font.render('Йети уселся пить чай.', True, (255,255,255))
text11 = font.render('А затем пошёл погулять.', True, (255,255,255))
text10 = font.render('А где тыква?', True, (255,255,255))
textYay = font.render('Йети вырастил тыкву, и со шкедами подружился', True, (255,255,255))
textRect = text.get_rect()
textRect2 = text2.get_rect()
textRect3 = text3.get_rect()
textRect4 = text4.get_rect()
textRect5 = text5.get_rect()
textRect6 = text6.get_rect()
textRect7 = text7.get_rect()
textRect8 = text8.get_rect()
textRect9 = text9.get_rect()
textRect10 = text10.get_rect()
textYay_Rect = textYay.get_rect()
textRect11 = text11.get_rect()
textwinrect = textwin.get_rect()
textRect.y = 10
textRect.x = 100
textRect2.y = 10
textRect2.x = 100
textRect3.y = 10
textRect3.x = 100
textRect4.y = 280
textRect4.x = 550
textRect5.y = 10
textRect5.x = 100
textRect6.y = 10
textRect6.x = 100
textRect7.y = 30
textRect7.x = 100
textRect8.y = 30
textRect8.x = 100
textRect9.y = 30
textRect9.x = 100
textRect10.y = 30
textRect10.x = 100
textRect11.y = 30
textRect11.x = 100
textYay_Rect.y = 30
textYay_Rect.x = 100
textwinrect.y = 30
textwinrect.x = 100
indoors = pygame.image.load('pics/indoors.png')
indoors = pygame.transform.scale(indoors, (300, 300))
indoors_rect = indoors.get_rect()
indoors_rect.x = 100
indoors_rect.y = 100
indoors3 = pygame.image.load('pics/indoors3.png')
indoors3 = pygame.transform.scale(indoors3, (300, 300))
indoors3_rect = indoors3.get_rect()
indoors2 = pygame.image.load('pics/indoors2.png')
indoors2 = pygame.transform.scale(indoors2, (300, 300))
indoors2_rect = indoors.get_rect()
indoors22 = pygame.image.load('pics/indoors22.png')
indoors22 = pygame.transform.scale(indoors22, (300, 300))
indoors2_rect2 = indoors.get_rect()
indoors23 = pygame.image.load('pics/indoors23.png')
indoors23 = pygame.transform.scale(indoors23, (300, 300))
indoors2_rect3 = indoors.get_rect()
bedroom = pygame.image.load('pics/bedroom.png')
bedroom = pygame.transform.scale(bedroom, (300, 300))
bedroom_rect = bedroom.get_rect()
bedroom2 = pygame.image.load('pics/bedroom2.png')
bedroom2 = pygame.transform.scale(bedroom2, (300, 300))
bedroom2_rect = bedroom2.get_rect()
bedroom3 = pygame.image.load('pics/bedroom3.png')
bedroom3 = pygame.transform.scale(bedroom3, (300, 300))
bedroom3_rect = bedroom3.get_rect()
kitchen = pygame.image.load('pics/kitchen.png')
kitchen = pygame.transform.scale(kitchen, (300, 300))
kitchen_rect = kitchen.get_rect()
kitchen2 = pygame.image.load('pics/kitchen2.png')
kitchen2 = pygame.transform.scale(kitchen2, (300, 300))
kitchen_rect2 = kitchen.get_rect()
kitchen3 = pygame.image.load('pics/kitchen3.png')
kitchen3 = pygame.transform.scale(kitchen3, (300, 300))
kitchen_rect3 = kitchen3.get_rect()
bathroom = pygame.image.load('pics/bathroom.png')
bathroom = pygame.transform.scale(bathroom, (300, 300))
bathroom_rect = bathroom.get_rect()
bathroom2 = pygame.image.load('pics/bathroom2.png')
bathroom2 = pygame.transform.scale(bathroom2, (300, 300))
bathroom_rect2 = bathroom2.get_rect()
bathroom3 = pygame.image.load('pics/bathroom3.png')
bathroom3 = pygame.transform.scale(bathroom3, (300, 300))
bathroom_rect3 = bathroom3.get_rect()
indoors3_rect.x = 100
indoors3_rect.y = 100
indoors2_rect.x = 100
indoors2_rect.y = 100
indoors2_rect2.x = 100
indoors2_rect2.y = 100
indoors2_rect3.x = 100
indoors2_rect3.y = 100
bedroom_rect.x = 100
bedroom_rect.y = 100
bedroom2_rect.x = 100
bedroom2_rect.y = 100
bedroom3_rect.x = 100
bedroom3_rect.y = 100
bathroom_rect.x = 100
bathroom_rect.y = 81
bathroom_rect2.x = 100
bathroom_rect2.y = 81
bathroom_rect3.x = 100
bathroom_rect3.y = 81
kitchen_rect.x = 100
kitchen_rect.y = 82
kitchen_rect2.x = 100
kitchen_rect2.y = 82
kitchen_rect3.x = 100
kitchen_rect3.y = 82
sadYeti = pygame.image.load('pics/sadYeti.png')
sadYeti = pygame.transform.scale(sadYeti, (300, 300))
sadYeti_rect = sadYeti.get_rect()
sadYeti_rect.x = 100
sadYeti_rect.y = 100
YotieHouse = pygame.image.load('pics/YotieHouse.png')
YotieHouse = pygame.transform.scale(YotieHouse, (640, 480))
YotieHouse_rect = YotieHouse.get_rect()
YotieHouse2 = pygame.image.load('pics/YotieHouse2.png')
YotieHouse2 = pygame.transform.scale(YotieHouse2, (640, 480))
YotieHouse2_rect = YotieHouse2.get_rect()
YotieHouse22 = pygame.image.load('pics/YotieHouse22.png')
YotieHouse22 = pygame.transform.scale(YotieHouse22, (640, 480))
YotieHouse2_rect2 = YotieHouse22.get_rect()
YotieHouse23 = pygame.image.load('pics/YotieHouse23.png')
YotieHouse23 = pygame.transform.scale(YotieHouse23, (640, 480))
YotieHouse23_rect = YotieHouse23.get_rect()
cat1 = pygame.image.load('pics/cat1.png')
cat1_rect = cat1.get_rect()
cat2 = pygame.image.load('pics/cat2.png')
cat2_rect = cat2.get_rect()
x2 = 10
y2 = 299
dx2 = 1
cat1_rect.x = x2
cat1_rect.y = y2
cat2_rect.x = x2
cat2_rect.y = y2
Running = True
while Running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    if curmode == 1:
        keys = pygame.key.get_pressed()
        frame2 += 1
        if keys[pygame.K_SPACE]:
            frame2 = 1200
        if frame2 < 150:
            # дом йети
            screen.blit(YotieHouse,YotieHouse_rect)
            screen.blit(text, textRect)
        elif frame2 < 300:
            screen.fill(black)
            screen.blit(indoors,indoors_rect)
            screen.blit(text2, textRect2)
        elif frame2 < 450:
            screen.fill(black)
            screen.blit(indoors,indoors_rect)
            screen.blit(text3, textRect3)
        elif frame2 < 500:
            screen.blit(indoors,indoors_rect)
            screen.blit(text4, textRect4)
        elif frame2 < 550:
            textRect4.y = 300
            screen.blit(text4, textRect4)
        elif frame2 < 600:
            textRect4.y = 320
            screen.blit(text4, textRect4)
        elif frame2 < 700:
            screen.blit(indoors3, indoors3_rect)
            yetir2_rect.x = 140 + frame3
            yetir2_rect.y = 289
            yetir1_rect.x = 140 + frame3
            yetir1_rect.y = 289
            frame3 += 2
            frame4 += 1
            if frame4 < 10:
                screen.blit(yetir2, yetir2_rect)
            if frame4 >= 10:
                screen.blit(yetir1, yetir1_rect)
            if frame4 >= 20:
                frame4 = 0
        elif frame2 < 900:
            #Дети
            yeti_standing_r_rect.x = 300
            yeti_standing_r_rect.y = 300
            screen.blit(YotieHouse2, YotieHouse2_rect)
            screen.blit(yeti_standing_r, yeti_standing_r_rect)
            screen.blit(text5, textRect5)
            screen.blit(text7, textRect7)
        elif frame2 < 1000:
            #Дети
            yeti_standing_r_rect.x = 300
            yeti_standing_r_rect.y = 300
            screen.blit(YotieHouse2, YotieHouse2_rect)
            screen.blit(yeti_standing_r, yeti_standing_r_rect)
            screen.blit(text8, textRect8)

        elif frame2 < 1100:
            screen.fill((0,0,0))
            screen.blit(indoors2, indoors2_rect)
            yetil2_rect.x = 210 + frame3
            yetil2_rect.y = 289
            yetil1_rect.x = 210 + frame3
            yetil1_rect.y = 289
            frame3 -= 2
            frame4 += 1
            if frame4 < 10:
                screen.blit(yetil2, yetil2_rect)
            if frame4 >= 10:
                screen.blit(yetil1, yetil1_rect)
            if frame4 >= 20:
                frame4 = 0
        elif frame2 < 1200:
            screen.fill((0,0,0))
            screen.blit(text6, textRect6)
            screen.blit(sadYeti, sadYeti_rect)
        else:
            curmode = 2
    if curmode == 2:
        if not key_collected and iscollide(x,y,key_rect.x,key_rect.y) and dl == 2:
            showhint('Йети подобрал ключ...')
            key_collected = True
        if not scissors_collected and iscollide(x,y,scissors_rect.x,scissors_rect.y) and key_collected and dl == 4:
            showhint('Йети подобрал ножницы...')
            scissors_collected = True
        if not food_collected and iscollide(x,y,food_rect.x,food_rect.y) and scissors_collected and dl == 3:
            showhint('Йети подобрал корм для котов...(догадались для чего?)')
            food_collected = True
        if not bovel_collected and iscollide(x,y,bovel_rect.x,bovel_rect.y) and food_collected and dl == 3:
            showhint('Йети насыпал корм коту')
            bovel = pygame.image.load('pics/bovel2.png')
            bovel_collected = True
        yetil1_rect.y = y
        yetil1_rect.x = x
        yetil2_rect.y = y
        yetil2_rect.x = x
        yetir1_rect.y = y
        yetir1_rect.x = x
        yetir2_rect.y = y
        yetir2_rect.x = x   
        yeti_standing_l_rect.x = x
        yeti_standing_l_rect.y = y
        yeti_standing_r_rect.x = x
        yeti_standing_r_rect.y = y
        dx = 0
        frame += 1
        screen.fill(black)
        if  dl == 1:
            draw_hall(indoors2, indoors2_rect, indoors22, indoors2_rect2, indoors23, indoors2_rect3)
            if x < 100:
                dl = 2
                x = 348
            if x > 348:
                x = 300
                dl = 6
        if dl == 2:
            draw_bedroom(bedroom, bedroom_rect, key, key_rect, seed, seed_rect, bedroom2, bedroom2_rect, bedroom3, bedroom3_rect)
            if x > 348:
                dl = 1
                x = 100
            if x < 100:
                dl = 3
                x = 348
        if dl == 3:
            draw_kitchen(kitchen, kitchen_rect, frame5, kitchen2, kitchen_rect2, kitchen3, kitchen_rect3, bovel, bovel_rect, food, food_rect, knife, knife_rect, wateringCan, wateringCan_rect)
            if x > 348:
                dl = 2
                x = 100
            if x < 100:
                dl = 4
                x = 348
        if dl == 4:
            draw_bathroom(bathroom, bathroom_rect, bathroom2, bathroom_rect2,bathroom3, bathroom_rect3, scissors, scissors_rect, fens, fens_rect)
            if x > 348:
                dl = 3
                x = 100
            if x < 100:
                x = 100
        if dl == 6:
            draw_outside(YotieHouse, YotieHouse_rect, YotieHouse22, YotieHouse2_rect2,YotieHouse23, YotieHouse23_rect, pumpkin, pumpkin_rect)
            if x < 300:
                dl = 1
                x = 348
            if x > 600:
                x = 600
        if frame > 20:
            frame = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            dx = 1
        if keys[pygame.K_LEFT]:
            dx = -1
        if keys[pygame.K_UP]:
            if y >= 289:
                dy = 1
            
        x = x + dx
        y = y - dy
        dy -= 1/80
        if y >= 289:
            dy = 0
            y = 289
        if dx < 0:
            if frame < 10:
                screen.blit(yetil1, yetil1_rect)
            else:
                screen.blit(yetil2, yetil2_rect)
        if dx > 0:
            if frame < 10:
                screen.blit(yetir1, yetir1_rect)
            else:
                screen.blit(yetir2, yetir2_rect)
        if dx == 0:
            if frame < 10:
                screen.blit(yeti_standing_l, yeti_standing_l_rect)
            else:
                screen.blit(yeti_standing_r, yeti_standing_r_rect)
        if bovel_collected:
            if iscollide(bovel_rect.x, bovel_rect.y,x2,y2):
                time.sleep(2)
                screen.blit(textwin, textwinrect)
                dx2 = 0
                screen.fill(black)
                screen.blit(YotieHouse, YotieHouse_rect)
                screen.blit(textwin, textwinrect)
                pygame.display.flip()
                curmode = 3
                time.sleep(10)
    if curmode == 3:
        frame7 += 1
        if frame7 < 300:
            screen.fill(black)
            screen.blit(indoors, indoors_rect)
            screen.blit(text9, textRect9)
        elif frame7 < 600:
            screen.fill(black)
            screen.blit(indoors2, indoors2_rect)
            screen.blit(text11, textRect11)
            yetir2_rect.x = 140 + frame3
            yetir2_rect.y = 289
            yetir1_rect.x = 140 + frame3
            yetir1_rect.y = 289
            frame3 += 0.8
            frame4 += 0.4
            if frame4 < 10:
                screen.blit(yetir2, yetir2_rect)
            if frame4 >= 10:
                screen.blit(yetir1, yetir1_rect)
            if frame4 >= 20:
                frame4 = 0
        elif frame7 < 610:
            yeti_standing_r_rect.x = 300
            yeti_standing_r_rect.y = 300
            screen.blit(YotieHouse, YotieHouse_rect)
            screen.blit(yeti_standing_r, yeti_standing_r_rect)
            screen.blit(text10, textRect10)
        elif frame7 < 1200:
            curmode = 4
    if curmode == 4:
        if not seed_collected and iscollide(x,y,seed_rect.x,seed_rect.y) and dl == 2:
            showhint('Йети подобрал семя')
            seed_collected = True
        if not wateringCan_collected and iscollide(x,y,wateringCan_rect.x,wateringCan_rect.y) and seed_collected == True and dl == 3 and seed_used:
            showhint('Йети взял лейку')
            wateringCan_collected = True
        if not fens_collected and iscollide(x,y,fens_rect.x,fens_rect.y) and wateringCan_collected == True and dl == 4 and wateringCan_used:
            showhint('Йети собрал доски для забора')
            fens_collected = True
        if not knife_collected and iscollide(x,y,knife_rect.x,knife_rect.y) and fens_collected == True and dl == 3 and fens_used:
            showhint('Йети взял ножик(для мордочки у тыквы)')
            knife_collected = True
        if iscollide(x, y, pumpkin_rect.x, pumpkin_rect.y) and seed_collected == True and dl == 6 and seed_used == False:
            seed_used = True
            showhint('Йети посадил семя')
        if iscollide(x, y, pumpkin_rect.x, pumpkin_rect.y) and wateringCan_collected == True and dl == 6 and wateringCan_used == False:
            wateringCan_used = True
            showhint('Йети полил тыкву')
        if radio == False and wateringCan_used and dl == 1:
            radio = True
            showhint('Внимание! Подростки начали нападать на тыквы.')
            screen.blit(YotieHouse22, YotieHouse2_rect2)
            showhint('Йети решил поставить забор чтобы защитить тыкву')
        if iscollide(x, y, pumpkin_rect.x, pumpkin_rect.y) and fens_collected == True and dl == 6 and fens_used == False:
            fens_used = True
            fens_blit = True
            showhint('Йети поставил забор.О и тыква как раз подросла!')
        if iscollide(x, y, pumpkin2_rect.x, pumpkin2_rect.y) and knife_collected == True and dl == 6 and knife_used == False:
            knife_used = True
            showhint('Йети вырезал мордочку')
        if knife_used == True:
            curmode = 5
        key_collected = False
        scissors_collected = False
        food_collected = False
        bovel_collected = False
        yetil1_rect.y = y
        yetil1_rect.x = x
        yetil2_rect.y = y
        yetil2_rect.x = x
        yetir1_rect.y = y
        yetir1_rect.x = x
        yetir2_rect.y = y
        yetir2_rect.x = x   
        yeti_standing_l_rect.x = x
        yeti_standing_l_rect.y = y
        yeti_standing_r_rect.x = x
        yeti_standing_r_rect.y = y
        screen.fill(black)
        if  dl == 1:
            draw_hall(indoors2, indoors2_rect, indoors22, indoors2_rect2, indoors23, indoors2_rect3)
            if x < 100:
                dl = 2
                x = 348
            if x > 348:
                x = 300
                dl = 6
        if dl == 2:
            draw_bedroom(bedroom, bedroom_rect, key, key_rect, seed, seed_rect, bedroom2, bedroom2_rect, bedroom3, bedroom3_rect)
            if x > 348:
                dl = 1
                x = 100
            if x < 100:
                dl = 3
                x = 348
        if dl == 3:
            draw_kitchen(kitchen, kitchen_rect, frame5, kitchen2, kitchen_rect2, kitchen3, kitchen_rect3, bovel, bovel_rect, food, food_rect, knife, knife_rect, wateringCan, wateringCan_rect)
            if x > 348:
                dl = 2
                x = 100
            if x < 100:
                dl = 4
                x = 348
        if dl == 4:
            draw_bathroom(bathroom, bathroom_rect, bathroom2, bathroom_rect2,bathroom3, bathroom_rect3, scissors, scissors_rect, fens, fens_rect)
            if x > 348:
                dl = 3
                x = 100
            if x < 100:
                x = 100
        if dl == 6:
            draw_outside(YotieHouse, YotieHouse_rect, YotieHouse22, YotieHouse2_rect2,YotieHouse23, YotieHouse23_rect, pumpkin, pumpkin_rect, fens, fens_rect, pumpkin2, pumpkin2_rect)
            if x < 300:
                dl = 1
                x = 348
            if x > 600:
                x = 600
        dx = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            dx = 1
        if keys[pygame.K_LEFT]:
            dx = -1
        if keys[pygame.K_UP]:
            if y >= 289:
                dy = 1
        frame += 1
        x = x + dx
        y = y - dy
        dy -= 1/80
        if y >= 289:
            dy = 0
            y = 289
        if dx < 0:
            if frame < 10:
                screen.blit(yetil1, yetil1_rect)
            else:
                screen.blit(yetil2, yetil2_rect)
        if dx > 0:
            if frame < 10:
                screen.blit(yetir1, yetir1_rect)
            else:
                screen.blit(yetir2, yetir2_rect)
        if dx == 0:
            if frame < 10:
                screen.blit(yeti_standing_l, yeti_standing_l_rect)
            else:
                screen.blit(yeti_standing_r, yeti_standing_r_rect)
        if frame > 20:
            frame = 0
    if curmode == 5:
        yeti_standing_r_rect.x = 300
        yeti_standing_r_rect.y = 300
        screen.blit(YotieHouse2, YotieHouse2_rect)
        screen.blit(yeti_standing_r, yeti_standing_r_rect)
        screen.blit(textYay, textYay_Rect)
        
    pygame.display.flip()
    time.sleep(1/60)