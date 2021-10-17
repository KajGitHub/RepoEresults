# -*- coding: utf-8 -*-
import csv
import sys
import datetime

def get_seconds(result):
    result_format = result.split(":")
    if (len(result_format) == 2):
        dt = datetime.datetime.strptime(result, "%M:%S")
        a_timedelta = dt - datetime.datetime(1900, 1, 1)
        seconds = a_timedelta.total_seconds()
        secs = str(seconds).split('.')[0]
    elif (len(result_format) == 3):
        dt = datetime.datetime.strptime(result, "%H:%M:%S")
        a_timedelta = dt - datetime.datetime(1900, 1, 1)
        seconds = a_timedelta.total_seconds()
        secs = str(seconds).split('.')[0]
    else:
        secs = ("HYL")
    return secs

def read_result(name):
    with open(sys.argv[2], 'r') as csv_results:
        csv_reader = csv.reader(csv_results, delimiter=';')
        for row in csv_reader:
            exist = 0
            if (row[1] == name):
                exist = 1
                return row[3]

with open(sys.argv[1], 'r') as csv_ilmo:
    csv_reader = csv.reader(csv_ilmo, delimiter=';')
    ssl_file = open("ssl.txt", "w")
    for row in csv_reader:
        if
            result = read_result(row[2])
            seconds = get_seconds(result)
            print(f'\t{row[1]:0>6}{row[2]:<23}{row[3]:<8}{row[0]:<10}{seconds:0>6}',file=ssl_file)
    ssl_file.close()
