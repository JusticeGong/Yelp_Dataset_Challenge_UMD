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
                w.write('<?xml version="1.0" encoding="UTF-8"?>\n')
                w.write('<markers>\n')
                for a in s:
                    a = a.replace("'", "")
                    a = a.replace("&", "")
                    a = a.split(',')
                    n = n + 1
                    try:
                        w.write('\t<marker id = "' + str(n) + '" name = "' + str(a[1]) + '" address = "' + str(a[4]) + ',' + str(a[5]) + ',' + str(a[6]) + '" lat = "' + str(a[2]) + '" lng = "' + str(a[3]) + '" type="restaurant"/>\n')
                    except:
                        1
            w.write('</markers>')
            w.close()
        r.close()