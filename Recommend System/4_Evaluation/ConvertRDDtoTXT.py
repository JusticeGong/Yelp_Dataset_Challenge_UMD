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
        index = str(i) + str(j)
        with open('D:/Workplace/BigData/DataTrim/RawEvaluation/PredOutput'+index+'.txt', 'r', encoding='utf8') as r:
            with open('D:/Workplace/BigData/DataTrim/Evaluation/PredOutput'+index+'.txt', 'w', encoding='utf8') as w:
                a = r.read()
                a = a.strip()
                a = a.split(')), ((')
                for b in a:
                    b = b.replace('[','')
                    b = b.replace(']', '')
                    b = b.replace('(', '')
                    b = b.replace(')', '')
                    w.write(str(b)+'\n')
                    n = n + 1
                    print(i,j,n)
                w.close()
            r.close()