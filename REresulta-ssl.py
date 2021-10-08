# -*- coding: utf-8 -*-
# avataan ilmo tiedosto ja tulostiedosto
# 1.Luupissa
#   1. Haetaan tuloksista nimi ja aika
#   2. Etsitään ilmosta nimellä
#       a. Saadaan lisenssi, seura, sarja
#   3. Generoidaan ssl-tulos rivi ja lisätään ssl tiedostoon

nimiT = "a"

aikasecT = "b"
nimiI= "c"

lisenssiI = "d"

seuraI = "e"
sarjaI = "f"
tiedosto_ssl = open("./outputs/ssl.txt", "w")

infile_ilmo = open("inputs/ilmoittautumiset2.csv", 'r')

def lue_ilmo(nimiT, rivi2):
        nimiI = ""
        sarjaI = ""
        lisenssiI = ""
        seuraI = ""
        loytyi = False


        rivi2 = rivi2.replace("\n", "")
        osat2 = rivi2.split(",")
        nimiI = osat2[2]

        if nimiI == nimiT:
        #Löytyi nimi yhtäläisyys
            sarjaI = osat2[0]
            lisenssiI = osat2[1]
            seuraI = osat2[3]
            loytyi = True
        return nimiI, sarjaI, lisenssiI, seuraI, loytyi


def lue_tulos():
#Avataan tulostiedosto ja luetaan tiedot
    with open("inputs/t20181017.csv", 'r') as infile_tulos:

        #Luetaan tuloksista nimet järjestyksessä, niin saadaan ssl-filuun valmiiksi oikeaan järjestykseen.
        #Otetaan nimi rivi kerrallaan ja sitten etsitään ilmoittautuneista loput puuttuvat tiedot (lisenssi, seura)
        for rivi in infile_tulos:
            osat = rivi.split(";")
            if osat[0] == "rata":
                continue
            rivi = rivi.replace("\n", "")
            sarjaT = osat[0]
            nimiT = osat[2]
            emitT = osat[4]
            aikaT = osat[6]
            min = aikaT.split(":")
            minuutti = int(min[0])
            sekuntti = int(min[1])
            aikasecT = "00" + str((minuutti * 60) + sekuntti)

            for rivi2 in infile_ilmo:
                nimiI, sarjaI, lisenssiI, seuraI, loytyi = lue_ilmo(nimiT, rivi2)
#                print("*******")
#                print(lisenssiI,nimiI, seuraI, sarjaI, "   ",aikasecT)
#                print("*******")
                data = lisenssiI + nimiI +"     " + seuraI + "    " + sarjaI + "   " + aikasecT
                tiedosto_ssl.write(data + "\n")
                if loytyi == True:
                    break
    return nimiT, aikasecT


lue_tulos()

print("*** Ja valmista tuli ***")
tiedosto_ssl.close()

ssl_txt = open("outputs/ssl.txt")
lines = ssl_txt.readlines()
for line in lines:
    print(line)
ssl_txt.close()
