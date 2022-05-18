# -*- coding: utf-8 -*-
import csv
import sys
import datetime

# Avataan tulos tiedosto ja haetaan nimellä tulosta
def read_result(name):
    with open(sys.argv[2], 'r') as csv_results:
        csv_reader = csv.reader(csv_results, delimiter=';')
        for row in csv_reader:
            if (row[1] == name): # jos nimi löytyy tuloksista
                result = row[3].replace(':', '') # poista : ajasta (esim: 1:25:33 => 12533)
                return result # palauttaa kilpailijan tuloksen pääohjelmaan
    csv_results.close()

# Helppi
if (len(sys.argv) != 3):
    print("\nScripti tarvitsee 2 argumenttia!\n")
    print("1. Irman ilmoittautumis tiedosto CSV muodossa.")
    print("2. EResults lite v3 tulos tiedoston CSV muodossa.\n")
    print("ESIM: python DoSll.py ilmoittautuneet.csv tulokset.csv\n")
    exit()

# Pääohjelma
# Avataan ilmoittautuneet tiedosto joka on saatu Irmasta
with open(sys.argv[1], 'r') as csv_ilmo:
    csv_reader = csv.reader(csv_ilmo, delimiter=';')
    ssl_file = open("ssl.csv", "w") # luodaan ssl.csv tiedosto johon lisätään ilmoittautuneet ja tulokset
    writer = csv.writer(ssl_file)
    for row in csv_reader:
        result = read_result(row[2]) # Haetaan tulos kilpailijalle nimellä tulos tiedostosta
        if result is None: # Jos kilpailijaa ei löydy tuloksista merkitään ei lähteneeksi (EIL)
            data = [row[1], row[2], row[3], row[0], "EIL"]
            writer.writerow(data) # kirjoitetaan kilpailija tiedot ja tulos ssl.csv tiedostoon
        elif result == "": # Jos kilpailijan aikaa ei löydy merkitään hylätyksi (HYL)
            data = [row[1], row[2], row[3], row[0], "HYL"]
            writer.writerow(data) # kirjoitetaan kilpailija tiedot ja tulos ssl.csv tiedostoon
        else: # kilpailijalle löytyi tulos tulostiedostosta
            data = [row[1], row[2], row[3], row[0], result]
            writer.writerow(data) # kirjoitetaan kilpailija tiedot ja tulos ssl.csv tiedostoon
    ssl_file.close()
csv_ilmo.close()

# Avataan ssl.csv tiedosto
ssl_csv_file = [line.split(',') for line in open('ssl.csv', 'r')]
# sortataan data ensin sarjan mukaan ja sitten sarjat tulosten mukaan
ssl_csv_file.sort(key = lambda x: (x[3], x[4]))
# kirjoitetaan sortattu data ssl.txt tiedostoon
with open("ssl.txt", "w") as ssl_txt_file:
    for row in ssl_csv_file:
        #f.write(";".join(item))
        row[4] = row[4].replace('\r', '').replace('\n', '') # poistetaan viimeisestä sarakkeesta rivin vaihto
        if (row[4] == "HYL"): # hylätty (HYL)
            print(f'{row[0]:0>6}{row[1]:<23}{row[2]:<8}{row[3]:<10}{row[4]:<6}', file=ssl_txt_file)
        elif (row[4] == "EIL"): # ei lähtenyt (EIL)
            print(f'{row[0]:0>6}{row[1]:<23}{row[2]:<8}{row[3]:<10}{row[4]:<6}', file=ssl_txt_file)
        else:
            # Kirjoitetaan tulos ssl.txt tiedostoon
            # row[1] lisenssinumero 6 merkkiä, jos on lyhyempi kuin 6 merkkiä niin täytetään nollia eteen (:0>6)
            # row[2] nimi 23 merkkiä, täytetään vasemmalta (:<23)
            # row[3] seura 8 merkkiä, täytetään vasemmalta (:<8)
            # row[0] sarja 10 merkkiä, täytetään vasemmalta (:<10)
            # seconds on tulos sekunteina 6 merkkiä, täytetään oikealta ja lisätään nollat eteen (:0>6)
            print(f'{row[0]:0>6}{row[1]:<23}{row[2]:<8}{row[3]:<10}{row[4]:0>6}', file=ssl_txt_file)
ssl_txt_file.close()
    # To Do
    # EIL vain monipäiväkisassa
    # EIL yhden päivän kisassa pitäisi vain jättää pois tuloksista?
    # Ilmoittautuneet.csv pitää olla solut puolipilkuilla eroteltuna
    # Tulos tiedostossa pitää olla tyhjissäkin riveissä erottimet esim. ;;;;
