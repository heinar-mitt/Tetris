import pygame

veerud = 10
read = 20
mängu_laius = 300
mängu_kõrgus = 600
block = 30              #üks tetrise ruut
mx = 20                 #mängu x-telje algus
my = 70                 #mängu y-telje algus

def loo_mänguväli(täidetud_positsioon={}):
    global mänguväli
    mänguväli = [[(0,0,0) for e in range(10)] for e in range(20)]       #luuakse list, mis koosneb 20-st reast ja 10-st veerust (0,0,0 on RGB värvid)
    for y in range(read):
        for x in range(veerud):
            if (x, y) in täidetud_positsioon:                           #otsime, kas asukohal x,y on juba mingi värv, kasutades sõnastikku, kus x,y on võti
                värvime = täidetud_positsioon[(x, y)]       
                mänguväli[y][x] = värvime                               #värvime mänguvälja x,y koha leitud värvi
    return mänguväli

def ruudistik(põhi, rida, veerg):
    for horisontaal in range(rida):
        pygame.draw.line(põhi, (128,128,128), (mx, my+ horisontaal*block), (mx + mängu_laius, my + horisontaal * block))                 #joonistab read
        for vertikaal in range(veerg):
            pygame.draw.line(põhi, (128,128,128), (mx + vertikaal * block, my), (mx + vertikaal * block, my + mängu_kõrgus))             #joonistab veerud

def joonista_järgmine_kujund(kujund, põhi):
    font = pygame.font.SysFont("simple", 30)
    silt = font.render("JÄRGMINE KUJUND:", 1, (10,10,10))

    x = 325                                                         #järgmise kujundi pildi asukoht x-teljel            
    y = 250                                                         #järgmise kujundi asukoht y-teljel

    asend = kujund.kujund[kujund.pööramine % len(kujund.kujund)]

    for i, joon in enumerate(asend):                                #enumerate määrab ära iga for indeksi järjestuse numbri
        rida = list(joon)
        for j, veerg in enumerate(rida):
            if veerg == "0":
                pygame.draw.rect(põhi, kujund.värv, (x + j*block, y + i*block, block, block))

    põhi.blit(silt, (x+10, y-30))

def joonista_aken(põhi):
    põhi.fill((96,96,96))
    pygame.font.init()
    font = pygame.font.SysFont("simple", 60)                    
    silt = font.render("TETRIS", 1, (10,10,10))

    põhi.blit(silt, (20 + 300/2 - silt.get_width()/2, 30))      #sildi paigutus (silt, asukoht, font)

    for read in range(len(mänguväli)):
        for veerud in range(len(mänguväli[read])):
            pygame.draw.rect(põhi, mänguväli[read][veerud], (mx + veerud*block, my + read*block, block, block))
    
    pygame.draw.rect(põhi, (30,30,30), (mx, my, mängu_laius, mängu_kõrgus), 2)

    ruudistik(põhi, 20, 10)