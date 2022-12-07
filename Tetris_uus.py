import pygame
from kujundid import *
from mänguaken import *
from mängufunktsioonid import *
from testid import *

#globaalsed mängu andmed:
laius = 550
kõrgus = 690
mängu_laius = 300
mängu_kõrgus = 600
block = 30

def main(display):
    täidetud_positsioon = {}                            #sõnastik kõikidest täidetud ruutudest ning nende värvidest
    mänguväli = loo_mänguväli(täidetud_positsioon)
    muuda_kujundit = False
    run = True
    praegune_kujund = leia_kujund()
    järgmine_kujund = leia_kujund()
    aeg = pygame.time.Clock()
    kukkumise_aeg = 0
    kukkumiskiirus = 0.3

#mäng käib seniks, kuni tuleb sündmus quit
    while run:
        mänguväli = loo_mänguväli(täidetud_positsioon)
        kukkumise_aeg += aeg.get_rawtime()
        aeg.tick()

        if kukkumise_aeg/1000 >= kukkumiskiirus:
            kukkumise_aeg = 0
            praegune_kujund.y += 1
            if not (leidub_ruumi(praegune_kujund, mänguväli)) and praegune_kujund.y > 0:    #kontroll, kas kujund puutub põhjaga
                praegune_kujund.y -= 1                                                      #kui puutub, siis muuda_kujundit=True võimaldab järgmisel muudetud kujundil tekkida
                muuda_kujundit = True                                   

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:                                    #Kui vajutatakse mingit noolt, toimub vastav sündmus
                if event.key == pygame.K_LEFT:
                    praegune_kujund.x -= 1
                    if not leidub_ruumi(praegune_kujund, mänguväli) == True:    #kontroll, kas saab antud suunas liikuda
                        praegune_kujund.x += 1                                  #x-koordinaati mööda liiguatakse vasakule
                if event.key == pygame.K_RIGHT:
                    praegune_kujund.x += 1
                    if not leidub_ruumi(praegune_kujund, mänguväli) == True:
                        praegune_kujund.x -= 1          
                if event.key == pygame.K_UP:
                    praegune_kujund.pööramine = praegune_kujund.pööramine + 1  
                    if not leidub_ruumi(praegune_kujund, mänguväli) == True:
                        praegune_kujund.pööramine = praegune_kujund.pööramine - 1
                if event.key == pygame.K_DOWN:
                    praegune_kujund.y += 1
                    if not leidub_ruumi(praegune_kujund, mänguväli) == True:
                        praegune_kujund.y -= 1
                        
                #test1(praegune_kujund)
                #test2(praegune_kujund)
                #test4(praegune_kujund)
        kujundi_positsioon = muuda_kujundi_asendit(praegune_kujund)

        for i in range(len(kujundi_positsioon)):                                #kujundite värvimiseks, y>=0 on sellepärast, et muidu võib kujundi mõni osa tekkida mänguvälja põhja, enne kui kukkuma hakkab
            x, y = kujundi_positsioon[i]
            if y > -1:
                mänguväli[y][x] = praegune_kujund.värv

        if muuda_kujundit == True:                                              #kui kujund puutub põhjaga
            for pos in kujundi_positsioon:                                      #otsitakse selle asukoht
                p = (pos[0], pos[1])                                            #ning lisatakse see täidetud_positsiooni sõnastikku
                täidetud_positsioon[p] = praegune_kujund.värv                   
            praegune_kujund = järgmine_kujund
            järgmine_kujund = leia_kujund()
            muuda_kujundit = False
            eemalda = eemalda_read(mänguväli, täidetud_positsioon)
            eemalda
            #test3(eemalda)
        
        joonista_aken(display)
        joonista_järgmine_kujund(järgmine_kujund, display)
        pygame.display.update()

        if mäng_läbi(täidetud_positsioon) == True:
            run = False
    pygame.display.quit()

def main_menu(display):
    main(display)
 
display = pygame.display.set_mode((laius, kõrgus))
pygame.display.set_caption("TETRIS")
main_menu(display)  
