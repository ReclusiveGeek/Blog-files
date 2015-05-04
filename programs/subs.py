#!/bin/python3

import sys
import datetime



# need to add basic checks that the file exists

infile = sys.argv[1]
adjust = int(sys.argv[2])

adjust = adjust * -1

if infile[-3:] != 'srt':
    print('Not got the extension srt on the file ' + infile)
    sys.exit(1)

outfile = infile[:-3] + 'new.srt'

org = open(infile, 'r', encoding="latin-1")
out = open(outfile, 'w', encoding="latin-1")

for line in org:
    line = line.rstrip()
    if line.find('-->') > 8:
        # print()
        # print(line)
        temp = line.split(' --> ')
        # tmp1 = datetime.datetime.strptime(temp[0], "%H:%M:%S,%f")- datetime.timedelta(milliseconds=adjust)
        tmp1 = datetime.datetime.strftime(datetime.datetime.strptime(temp[0], "%H:%M:%S,%f")- datetime.timedelta(milliseconds=adjust),  "%H:%M:%S,%f")[:-3]
        # tmp2 = datetime.datetime.strptime(temp[1], "%H:%M:%S,%f") - datetime.timedelta(milliseconds=adjust)
        tmp2 = datetime.datetime.strftime(datetime.datetime.strptime(temp[1], "%H:%M:%S,%f") - datetime.timedelta(milliseconds=adjust),  "%H:%M:%S,%f")[:-3]
        new = str.join(' --> ', (tmp1, tmp2))
        out.write(new + '\n')
        # print(str(new))
    else:
        out.write(line + '\n')
out.close()
org.close()






