def test1(praegune_kujund):
    if praegune_kujund.x >= 0 and praegune_kujund.x < 10:
        print("Test 1 (kujundi liikumine x-teljel ning piirides püsimine) passed!")

def test2(praegune_kujund):
    if praegune_kujund.y <= 20:
        print("Test 2 (kujundi liikumine y-teljel ning piirides püsimine) passed!")

def test3(eemalda):
    if eemalda > 0:
        print("Test 3 (ridade eemaldus) passed.", "Eemaldati", eemalda, "rida")

def test4(praegune_kujund):
                    #kujundite_pöörded = {0: 1, 1: 1, 2: 2, 3: 0, 4: 3, 5: 3, 6: 3}
                    kraadid = {0: 0, 1: 90, 2: 180, 3: 270}
                    if len(praegune_kujund.kujund) == 0 or len(praegune_kujund.kujund) == 1:
                        if 0 <= kraadid[praegune_kujund.pööramine % len(praegune_kujund.kujund)] <= 90:
                            print("Test 4 passed!")
                        else:
                            print("Test 4 (kujund", len(praegune_kujund.kujund), ") failed!")
                    if len(praegune_kujund.kujund) == 2:
                        if 0 <= kraadid[praegune_kujund.pööramine % len(praegune_kujund.kujund)] <= 180:
                            print("Test 4 passed!")
                        else:
                            print("Test 4 (kujund", len(praegune_kujund.kujund), ") failed!")
                    if len(praegune_kujund.kujund) == 3:
                        if kraadid[praegune_kujund.pööramine % len(praegune_kujund.kujund)] == 0:
                            print("Test 4 passed!")
                        else:
                            print("Test 4 (kujund", len(praegune_kujund.kujund), ") failed!")
                    if len(praegune_kujund.kujund) == 4 or len(praegune_kujund.kujund) == 5 or len(praegune_kujund.kujund) == 6:
                        if 0 <= kraadid[praegune_kujund.pööramine % len(praegune_kujund.kujund)] <= 270:
                            print("Test 4 passed!")
                        else:
                            print("Test 4 (kujund", len(praegune_kujund.kujund), ") failed!")