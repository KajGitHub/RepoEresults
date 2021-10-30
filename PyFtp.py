# -*- coding: utf-8 -*-
import ftplib
import sys

host       = "whm51.louhi.net"
port       = 21
user       = "skpohjan"
pw         = "p0h1a2t3h4i"
localfile  = sys. argv[1]
remotefile = sys. argv[1]
ftpdir     = "/www/tulokset/"

ftp = ftplib.FTP()
ftp.connect(host, port)
print (ftp.getwelcome())
try:
    print ("Logging in...")
    ftp.login(user, pw)
    ftp.cwd(ftpdir)
    uploadfile = open(localfile, "rb")
    ftp.storlines('STOR %s' % remotefile, uploadfile)
    uploadfile.close()
except:
    "failed to login"
ftp.quit()
