# -*- coding: utf-8 -*-

import sys

# Avataan tiedosto komentoriviltä ja splitataan , erottimena rivit
lines = [line.split(',') for line in open(sys.argv[1], 'r')]
# sortataan data ensin kolumni 3 mukaan ja sitten kolumni 4 mukaan
lines.sort(key = lambda x: (x[3], x[4]))
# kirjoitetaan sortattu data ssl_sorted.txt tiedostoon
with open("ssl_sorted.txt", "w") as f:
    for item in lines:
        f.write(";".join(item))
