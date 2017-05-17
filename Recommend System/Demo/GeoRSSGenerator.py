import json
import re
import random
def sti(s):
    return str(abs(hash(str(s))) % (10 ** 8))


for i in range (1, 51):
    n = 0
    path = 'D:/Workplace/BigData/DataTrim/Demo/' + str(i) + '.xml'
    with open('D:/Workplace/BigData/DataTrim/Demo/business.txt', 'r', encoding="utf8") as r:
        with open(path, 'w', encoding="utf8") as w:
            for line in r:
                line = line.split('#')
                s = random.sample(line, 25)
                w.write('<?xml version="1.0" encoding="utf-8"?>\n')
                w.write('<feed>\n')
                w.write('<title>Yelp_Recommend</title>\n')
                for a in s:
                    a = a.replace("'", "")
                    a = a.replace("&", "")
                    a = a.split(',')
                    w.write('<entry>\n')
                    w.write('<title>' + a[1] + '</title>\n')
                    w.write('<id>' + a[0] + '</id>\n')
                    w.write('<summary>' + a[4] + '</summary>\n')
                    w.write('<georss:point>' + a[2] + ' ' + a[3] + '</georss:point>\n')
                    w.write('</entry>\n')
            w.write('</feed>\n')
            w.close()
        r.close()
