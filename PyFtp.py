# -*- coding: utf-8 -*-
import ftplib
import sys
import time

# Helppi
if (len(sys.argv) != 3):
    print('\nScripti tarvitsee 2 argumenttia!\n')
    print('1. Tiedosto, joka lähetetään serverille tästä samasta kansiosta, jossa ohjelma ajetaan.')
    print('2. Lähetysväli sekunteina.\n')
    print('ESIM: python PyFtp.py tulokset.html 60\n')
    exit()

# Käytetyt muuttujat
host       = 'whm51.louhi.net'
port       = 21
user       = 'skpohjan'
pw         = 'p0h1a2t3h4i'
localfile  = sys. argv[1]
remotefile = sys. argv[1]
ftpdir     = '/www/tulokset/'
sleep_time = sys. argv[2]

# FTP yhteyden muodostaminen ja tiedoston lähettäminen serverille
def ftp_connect():
    ftp = ftplib.FTP()
    ftp.connect(host, port)
    print (ftp.getwelcome())
    try:
        print ("Logging in...")
        ftp.login(user, pw)
        ftp.cwd(ftpdir)
        print ('Upload', localfile, 'to server')
        uploadfile = open(localfile, "rb")
        ftp.storlines('STOR %s' % remotefile, uploadfile)
        uploadfile.close()
    except:
        "failed to login"
        ftp.quit()

# Tauko sekunteina lähetysten välissä
def sleep():
    print ('Going to sleep for', sleep_time, 'seconds')
    for x in range(0, int(sleep_time)):
        time.sleep(1)
        print('.', end='', flush=True)
    print('\n')

# Pääohjelma
while True:
    ftp_connect()
    sleep()
