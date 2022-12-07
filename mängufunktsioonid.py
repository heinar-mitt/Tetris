def muuda_kujundi_asendit(kujund): 
    positsioonid = []
    asend = kujund.kujund[kujund.pööramine % len(kujund.kujund)]
    
    for i, joon in enumerate(asend):
        rida = list(joon)
        for j, veerg in enumerate(rida):
            if veerg == "0":
                positsioonid.append((kujund.x + j, kujund.y + i))
    
    for i, pos in enumerate(positsioonid):
        positsioonid[i] = (pos[0] - 2, pos[1] - 4)
    return positsioonid

def leidub_ruumi(kujund, mänguväli):
    lubatud_ala = [[(e, el) for e in range(10) if mänguväli[el][e] == (0,0,0)] for el in range(20)]       #list mängu alast [[()], [()], ...]
    lubatud_ala = [e for sub in lubatud_ala for e in sub]                                                 #paneme järjendid ühte listi, [(),()..]
    muudetud_kujund = muuda_kujundi_asendit(kujund)

    for pos in muudetud_kujund:
        if pos not in lubatud_ala:
            if pos[1] > -1:             #Kuna kujund alustab kukkumist väljaspool ala (on negatiivses alas), siis hakkame alles kontrolli tegema 0-positsioonist
                return False
    return True

def mäng_läbi(positsioonid):            #Kontrollib, kas kujundid puutuvad lage, ehk y>=0
    for pos in positsioonid:
        x, y = pos
        if y < 1:
            return True
    return False

def eemalda_read(mänguväli, täidetud_positsioon):
    juhtumid = 0
    for i in range(len(mänguväli)-1,-1,-1):
        mänguvälja_rida = mänguväli[i]
        if (0,0,0) not in mänguvälja_rida:
            juhtumid += 1
            index = i
            for j in range(len(mänguvälja_rida)):
                try:
                    del täidetud_positsioon[(j,i)]
                except ValueError:
                    continue
    if juhtumid > 0:
        for võti in sorted(list(täidetud_positsioon), key=lambda x: x[1])[::-1]:
            x, y = võti
            if y < index:
                uus_võti = (x, y + juhtumid)
                täidetud_positsioon[uus_võti] = täidetud_positsioon.pop(võti)
    return juhtumid

