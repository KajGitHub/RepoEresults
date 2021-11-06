# -*- coding: utf-8 -*-
import csv
import sys
import datetime

# Muutta ajan HH:MM:SS sekunneiksi
def get_seconds(result):
    result_format = result.split(":")
    if (len(result_format) == 2): # Jos kentässä on vain MM:SS niin lisätään 0 eteen 0:MM:SS ja muutetaan sekunneiksi
        dt = datetime.datetime.strptime(result, "%M:%S")
        a_timedelta = dt - datetime.datetime(1900, 1, 1)
        seconds = a_timedelta.total_seconds()
        secs = str(seconds).split('.')[0]
    elif (len(result_format) == 3): # Kenttä HH:MM:SS muutetaan sekunneiksi
        dt = datetime.datetime.strptime(result, "%H:%M:%S")
        a_timedelta = dt - datetime.datetime(1900, 1, 1)
        seconds = a_timedelta.total_seconds()
        secs = str(seconds).split('.')[0]
    else: # Jos löytyy tuloksista mutta ei aikaa niin laitetaan hylätyksi (HYL)
        secs = ("HYL")
    return secs # Palautetaan sekunnit pääohjelmaan

# Avataan tulos tiedosto ja haetaan nimellä tulosta
def read_result(name):
    with open(sys.argv[2], 'r') as csv_results:
        csv_reader = csv.reader(csv_results, delimiter=';')
        for row in csv_reader:
            if (row[1] == name):
                return row[3]

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
    ssl_file = open("ssl.txt", "w")
    for row in csv_reader:
        result = read_result(row[2]) # Haetaan tulos kilpailijalle nimellä tulos tiedostosta
        if result is None: # Jos kilpailijaa ei löydy tuloksista merkitään ei lähteneeksi (EIL)
            seconds = "EIL"
            print(f'{row[1]:0>6}{row[2]:<23}{row[3]:<8}{row[0]:<10}{seconds:<6}\r', file=ssl_file)
        else:
            seconds = get_seconds(result)
            if (seconds == "HYL"): # Jos kilpailija löytyy tuloksista mutta ei ole aikaa niin merkitään hylätyksi (HYL)
                print(f'{row[1]:0>6}{row[2]:<23}{row[3]:<8}{row[0]:<10}{seconds:<6}\r', file=ssl_file)
            else:
                # Kirjoitetaan tulos ssl.txt tiedostoon
                # row[1] lisenssinumero 6 merkkiä, jos on lyhyempi kuin 6 merkkiä niin täytetään nollia eteen (:0>6)
                # row[2] nimi 23 merkkiä, täytetään vasemmalta (:<23)
                # row[3] seura 8 merkkiä, täytetään vasemmalta (:<8)
                # row[0] sarja 10 merkkiä, täytetään vasemmalta (:<10)
                # seconds on tulos sekunteina 6 merkkiä, täytetään oikealta ja lisätään nollat eteen (:0>6)
                print(f'{row[1]:0>6}{row[2]:<23}{row[3]:<8}{row[0]:<10}{seconds:0>6}\r',file=ssl_file)
    ssl_file.close()
    # To Do
    # EIL vain monipäiväkisassa
    # järjestä ajan mukaan
