import random
with open('D:/Workplace/BigData/DataTrim/Demo/RandomUserGroup.txt', 'a', encoding='utf8') as w:
    for i in range(1, 8):
        path ='D:/Workplace/BigData/DataTrim/UserGroupList/QueryList3' + str(i) + '.txt'
        with open(path, 'r', encoding='utf8') as r:
            for line in r:
                line = line.replace(' ', '')
                line = line.split(',')
                rs = random.sample(line, int(len(line)/5000))
            for j in rs:
                w.write(j)
                w.write(',')
            r.close()
    w.close()
