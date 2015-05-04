#!/bin/python3

import sys
import datetime



# need to add basic checks that the file exists

if sys.argv[1] == '--help':
    print()
    print('Usage subs.py <file name> <millisecs>')
    print()
    print('   <file name>  is the name of the subtitle file and it must end have the file extension  .slt')
    print('   <millisecs> is the number of millisecs that you want the file adjusted by. To make the subtitles appear earlier and a - to the value ie to make then appear 2 secs earlier -2000 to make then appear 2 secs later 2000')
    print()
    print('A new file will be created with the extension .new.slt')
    print()
    sys.exit()


infile = sys.argv[1]
adjust = int(sys.argv[2])

# need to add basic checks that the file exists and what its encoded as.

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
        temp = line.split(' --> ')
        tmp1 = datetime.datetime.strftime(datetime.datetime.strptime(temp[0], "%H:%M:%S,%f")- datetime.timedelta(milliseconds=adjust),  "%H:%M:%S,%f")[:-3]
        tmp2 = datetime.datetime.strftime(datetime.datetime.strptime(temp[1], "%H:%M:%S,%f") - datetime.timedelta(milliseconds=adjust),  "%H:%M:%S,%f")[:-3]
        new = str.join(' --> ', (tmp1, tmp2))
        out.write(new + '\n')
    else:
        out.write(line + '\n')
out.close()
org.close()






