j = 0
for i in range(1, 4):
    if i == 1:
        j = 4
    elif i == 2:
        j =6
    else:
        j = 8
    for j in range (1, j):
        n = 0
        Dict = {}
        index = str(i) + str(j)
        with open('D:/Workplace/BigData/DataTrim/Evaluation/PredOutput'+index+'.txt', 'r', encoding='utf8') as rsmall:
            with open('D:/Workplace/BigData/DataTrim/Evaluation/MidOutput'+str(int(index)-1)+'.txt', 'r', encoding='utf8') as rbig:
                with open('D:/Workplace/BigData/DataTrim/Evaluation/MidOutput' + index + '.txt', 'w',
                          encoding='utf8') as w:
                    for lines in rsmall:
                        lines = lines.strip()
                        lines = lines.replace(' ', '')
                        lines = lines.replace('[', '')
                        lines = lines.replace(']', '')
                        lines = lines.replace("'", '')
                        lines = lines.split(',')
                        skey = str(lines[0])+str(lines[1])
                        Dict[skey] = str(lines[3])
                    for lineb in rbig:
                        lineb = lineb.strip()
                        lineb = lineb.replace(' ', '')
                        lineb = lineb.replace('[', '')
                        lineb = lineb.replace(']', '')
                        lineb = lineb.replace("'", '')
                        lineb = lineb.split(',')
                        bkey = str(lineb[0]) + str(lineb[1])
                        if bkey in Dict.keys():
                            lineb.append(Dict[bkey])
                        else:
                            lineb.append('0')
                        w.write(str(lineb) + '\n')
                        n = n + 1
                        print(i,j,n)
                    w.close()
                rbig.close()
            rsmall.close()