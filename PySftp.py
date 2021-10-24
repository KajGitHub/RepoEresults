
# -*- coding: utf-8 -*-
import sys
import pysftp
def sftpExample():
    try:
        cnopts = sftp.CnOpts()
        cnopts.hostkeys = None
        s = sftp.Connection(host='whm51.louhi.net', username='skpohjan', password='p0h1a2t3h4i',cnopts=cnopts)

        remotepath = '/www/tulokset/' + sys. argv[1]
        localpath = 'sys. argv[1]'
        s.put(localpath,remotepath)

        s.close()

    except Exception as e:
        print(e)
sftpExample()
