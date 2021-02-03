import pygame
import time
import random
pygame.init()
bait_x = 162
bait_y = 310
bait_int_x = int(bait_x)
bait_int_y = int(bait_y)
#gravity = 0
speed = 4
op = 1.5
caught = False
fishing = False
clock = pygame.time.Clock()
force_y = 1.5
fish = False
pufferfish_unlocked = False
gravity_force = 0
cod_unlocked = False
salmon_unlocked = False
inv = []
shark = pygame.image.load(r'C:\Users\48664\Desktop\FIshingSharkBeta\Fishing Shark BETA\shark2.png')
shark3 = pygame.image.load(r'C:\Users\48664\Desktop\FIshingSharkBeta\Fishing Shark BETA\shark3.png')
bait = pygame.image.load(r'C:\Users\48664\Desktop\FIshingSharkBeta\Fishing Shark BETA\bait.png')
shark4 = pygame.image.load(r'C:\Users\48664\Desktop\FIshingSharkBeta\Fishing Shark BETA\shark4.png')
port = pygame.image.load(r'C:\Users\48664\Desktop\FIshingSharkBeta\Fishing Shark BETA\port.png')
thing = pygame.image.load(r'C:\Users\48664\Desktop\FIshingSharkBeta\Fishing Shark BETA\thing.png')
cod = pygame.image.load(r'C:\Users\48664\Desktop\FIshingSharkBeta\Fishing Shark BETA\cod2.png')
salmon = pygame.image.load(r'C:\Users\48664\Desktop\FIshingSharkBeta\Fishing Shark BETA\salmon2_left.png')
salmon2 = pygame.image.load(r'C:\Users\48664\Desktop\FIshingSharkBeta\Fishing Shark BETA\salmon2.png')
carp = pygame.image.load(r'C:\Users\48664\Desktop\FIshingSharkBeta\Fishing Shark BETA\karp.png')
pufferfish = pygame.image.load(r'C:\Users\48664\Desktop\FIshingSharkBeta\Fishing Shark BETA\pufferfish.png')
star = pygame.image.load(r'C:\Users\48664\Desktop\FIshingSharkBeta\Fishing Shark BETA\star.png')
jelly = pygame.image.load(r'C:\Users\48664\Desktop\FIshingSharkBeta\Fishing Shark BETA\jelly.png')
screen = pygame.display.set_mode((1000,600))
carp_unlocked = False
star_unlocked = False
jelly_unlocked = False
fish_pos = []
fish1_x= 300
fish1_y= 465
fish2_x= 340
fish2_y=465
fish3_x= 360
fish3_y=445
pygame.display.set_icon(cod)
pygame.display.set_caption('Fishing Shark')
while True:
    while True:
        while True:
            clock.tick(100)
            caught = False
            fishing = False
            gravity_force = 0
            speed = 4
            bait_x = 162
            bait_y = 310
            bait_x = 162
            bait_y = 310
            bait_int_x = int(bait_x)
            bait_int_y = int(bait_y)
            screen.fill((0,10,50))
            screen.blit(port,(0,0))
            screen.blit(shark,(30,280))
            if cod_unlocked:
                screen.blit(cod,(cod_pos_x,cod_pos_y))
            if salmon_unlocked:
                screen.blit(salmon2,(salmon_pos_x,salmon_pos_y))
            if carp_unlocked:
                screen.blit(carp,(carp_pos_x,carp_pos_y))
            if pufferfish_unlocked:
                screen.blit(pufferfish,(pufferfish_pos_x,pufferfish_pos_y))
            if star_unlocked:
                screen.blit(star,(star_pos_x,star_pos_y))  #300,430
            if jelly_unlocked:
                screen.blit(jelly,(jelly_pos_x,jelly_pos_y))
            pygame.display.update()              
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    #time.sleep(1)
                    screen.fill((0,10,50))
                    screen.blit(port,(0,0))
                    screen.blit(shark3,(30,280))
                    if cod_unlocked:
                        screen.blit(cod,(cod_pos_x,cod_pos_y))
                    if salmon_unlocked:
                        screen.blit(salmon2,(salmon_pos_x,salmon_pos_y))
                    if carp_unlocked:
                        screen.blit(carp,(carp_pos_x,carp_pos_y))
                    if pufferfish_unlocked:
                        screen.blit(pufferfish,(pufferfish_pos_x,pufferfish_pos_y))
                    if star_unlocked:
                        screen.blit(star,(star_pos_x,star_pos_y))
                    if jelly_unlocked:
                        screen.blit(jelly,(jelly_pos_x,jelly_pos_y))
                    pygame.display.update()
                    time.sleep(1)
                    screen.fill((0,10,50))
                    screen.blit(port,(0,0))
                    screen.blit(shark4,(30,280))
                    if cod_unlocked:
                        screen.blit(cod,(cod_pos_x,cod_pos_y))
                    if salmon_unlocked:
                        screen.blit(salmon2,(salmon_pos_x,salmon_pos_y))
                    if carp_unlocked:
                        screen.blit(carp,(carp_pos_x,carp_pos_y))
                    if pufferfish_unlocked:
                        screen.blit(pufferfish,(pufferfish_pos_x,pufferfish_pos_y))
                    if star_unlocked:
                        screen.blit(star,(star_pos_x,star_pos_y))
                    if jelly_unlocked:
                        screen.blit(jelly,(jelly_pos_x,jelly_pos_y))
                        
                    pygame.display.update()
                    screen.fill((0,10,50))
                    screen.blit(port,(0,0))
                    screen.blit(shark4,(30,280))
                    if cod_unlocked:
                        screen.blit(cod,(cod_pos_x,cod_pos_y))
                    if salmon_unlocked:
                        screen.blit(salmon2,(salmon_pos_x,salmon_pos_y))
                    if carp_unlocked:
                        screen.blit(carp,(carp_pos_x,carp_pos_y))
                    if pufferfish_unlocked:
                        screen.blit(pufferfish,(pufferfish_pos_x,pufferfish_pos_y))
                    if star_unlocked:
                        screen.blit(star,(star_pos_x,star_pos_y))
                    if jelly_unlocked:
                        screen.blit(jelly,(jelly_pos_x,jelly_pos_y))
                    pygame.display.update()
                    for i in range(400):
                        clock.tick(1000)
                        screen.fill((0,10,50))
                        screen.blit(port,(0,0))
                        pygame.draw.line(screen,(0,0,0),(162,310),(bait_x,bait_y),(6))
                        screen.blit(shark4,(30,280))
                        screen.blit(bait,(bait_x,bait_y))
                        if cod_unlocked:
                            screen.blit(cod,(cod_pos_x,cod_pos_y))
                        if salmon_unlocked:
                            screen.blit(salmon2,(salmon_pos_x,salmon_pos_y))
                        if carp_unlocked:
                            screen.blit(carp,(carp_pos_x,carp_pos_y))
                        if pufferfish_unlocked:
                            screen.blit(pufferfish,(pufferfish_pos_x,pufferfish_pos_y))
                        if star_unlocked:
                            screen.blit(star,(star_pos_x,star_pos_y))
                        if jelly_unlocked:
                            screen.blit(jelly,(jelly_pos_x,jelly_pos_y))
                        pygame.display.update()
                        bait_x += 1
                        bait_y = bait_y - force_y - gravity_force
                        gravity_force -= 0.011
                        bait_int_x = int(bait_x)
                        bait_int_y = int(bait_y)
                        fishing = True

            while fishing:
                if caught:
                    break
                choice = random.randint(1,300000000)
                if choice > 0 and choice < 11:
                    fish = "cod"
                    screen.blit(cod,(bait_x-16,bait_y-16))
                    pygame.display.update()
                    if not cod_unlocked:
                        if len(inv) == 0:
                            cod_pos_x = 300
                            cod_pos_y = 465
                        if len(inv) == 1:
                            cod_pos_x = 340
                            cod_pos_y = 465
                        if len(inv) == 2:
                            cod_pos_x = 340
                            cod_pos_y = 445
                        if len(inv) == 3:
                            cod_pos_x = 245
                            cod_pos_y = 465
                        if len(inv) == 4:
                            cod_pos_x = 180
                            cod_pos_y = 465
                        if len(inv) == 5:
                            cod_pos_x = 300
                            cod_pos_y = 430
                    if not "cod" in inv:
                        inv.append("cod")
                    cod_unlocked = True
                    caught = True
                    time.sleep(1)
                if choice > 10 and choice < 21:
                    fish = "salmon"
                    screen.blit(salmon,(bait_x-16,bait_y-16))
                    pygame.display.update()
                    if not salmon_unlocked:
                        if len(inv) == 0:
                            salmon_pos_x = 300
                            salmon_pos_y = 465
                        if len(inv) == 1:
                            salmon_pos_x = 340
                            salmon_pos_y = 465
                        if len(inv) == 2:
                            salmon_pos_x = 340
                            salmon_pos_y = 445
                        if len(inv) == 3:
                            salmon_pos_x = 245
                            salmon_pos_y = 465
                        if len(inv) == 4:
                            salmon_pos_x = 180
                            salmon_pos_y = 465
                        if len(inv) == 5:
                            salmon_pos_x = 300
                            salmon_pos_y = 430
                    if not "salmon" in inv:
                        inv.append("salmon")
                    salmon_unlocked = True
                    caught = True
                    time.sleep(1)
                if choice > 20 and choice < 30:
                    fish = "carp"
                    screen.blit(carp,(bait_x-16,bait_y-16))
                    pygame.display.update()
                    if not carp_unlocked:
                        if len(inv) == 0:
                            carp_pos_x = 300
                            carp_pos_y = 465
                        if len(inv) == 1:
                            carp_pos_x = 340
                            carp_pos_y = 465
                        if len(inv) == 2:
                            carp_pos_x = 340
                            carp_pos_y = 445
                        if len(inv) == 3:
                            carp_pos_x = 245
                            carp_pos_y = 465
                        if len(inv) == 4:
                            carp_pos_x = 180
                            carp_pos_y = 465
                        if len(inv) == 5:
                            carp_pos_x = 300
                            carp_pos_y = 430
                    if not "carp" in inv:
                        inv.append("carp")
                    carp_unlocked = True
                    caught = True
                    time.sleep(1)
                if choice > 29 and choice < 33:
                    fish = "pufferfish"
                    screen.blit(pufferfish,(bait_x-16,bait_y-16))
                    pygame.display.update()
                    if not pufferfish_unlocked:
                        if len(inv) == 0:
                            pufferfish_pos_x = 300
                            pufferfish_pos_y = 465
                        if len(inv) == 1:
                            pufferfish_pos_x = 340
                            pufferfish_pos_y = 465
                        if len(inv) == 2:
                            pufferfish_pos_x = 340
                            pufferfish_pos_y = 445
                        if len(inv) == 3:
                            pufferfish_pos_x = 245
                            pufferfish_pos_y = 465
                        if len(inv) == 4:
                            pufferfish_pos_x = 180
                            pufferfish_pos_y = 465
                        if len(inv) == 5:
                            pufferfish_pos_x = 300
                            pufferfish_pos_y = 430
                    if not "pufferfish" in inv:
                        inv.append("pufferfish")
                    pufferfish_unlocked = True
                    caught = True
                    time.sleep(1)
                if choice > 32 and choice < 36:
                    fish = "star"
                    screen.blit(star,(bait_x-16,bait_y-16))
                    pygame.display.update()
                    if not star_unlocked:
                        if len(inv) == 0:
                            star_pos_x = 300
                            star_pos_y = 465
                        if len(inv) == 1:
                            star_pos_x = 340
                            star_pos_y = 465
                        if len(inv) == 2:
                            star_pos_x = 340
                            star_pos_y = 445
                        if len(inv) == 3:
                            star_pos_x = 245
                            star_pos_y = 465
                        if len(inv) == 4:
                            star_pos_x = 180
                            star_pos_y = 465
                        if len(inv) == 5:
                            star_pos_x = 300
                            star_pos_y = 430
                    if not "star" in inv:
                        inv.append("star")
                    star_unlocked = True
                    caught = True
                    time.sleep(1)
                if choice > 35 and choice < 37:
                    fish = "jelly"
                    screen.blit(jelly,(bait_x-16,bait_y-16))
                    pygame.display.update()
                    if not jelly_unlocked:
                        if len(inv) == 0:
                            jelly_pos_x = 300
                            jelly_pos_y = 465
                        if len(inv) == 1:
                            jelly_pos_x = 340
                            jelly_pos_y = 465
                        if len(inv) == 2:
                            jelly_pos_x = 340
                            jelly_pos_y = 445
                        if len(inv) == 3:
                            jelly_pos_x = 245
                            jelly_pos_y = 465
                        if len(inv) == 4:
                            jelly_pos_x = 180
                            jelly_pos_y = 465
                        if len(inv) == 5:
                            jelly_pos_x = 300
                            jelly_pos_y = 430
                    if not "jelly" in inv:
                        inv.append("jelly")
                    jelly_unlocked = True
                    caught = True
                    time.sleep(1)
                
                    #screen.fill((0,0,0))
                    #screen.blit(port,(0,0))
                    #pygame.draw.line(screen,(0,0,0),(162,310),(bait_x,bait_y),(6))
                    #screen.blit(shark4,(30,280))
                    #screen.blit(bait,(bait_x,bait_y))
                    #pygame.display.update()
                    
                    
                
                        
                        
                        
            
            
