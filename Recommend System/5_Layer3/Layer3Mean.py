index = ['13','25','37']
MSE = {}
MAPE = {}

for i in index:
    j = int(i[1])
    ipath = 'D:/Workplace/BigData/DataTrim/Evaluation/MSE/MidOutput' + i + '.txt'
    opath = 'D:/Workplace/BigData/DataTrim/Evaluation/MSE/L3MeanModelOutput' + i + '.txt'
    n = 0
    with open(ipath, 'r', encoding='utf8') as r:
        with open(opath, 'w', encoding='utf8') as w:
            for line in r:
                line = line.strip()
                line = line.split(',')
                sum = 0
                count = 0
                for k in range(3, 4 + j):
                    if float(line[k]) != 0:
                        sum = sum + float(line[k])
                        count = count + 1
                line[3] = str(sum/count)
                for p in range(0, 4):
                    w.write(line[p])
                    if p != 3:
                        w.write(',')
                    else:
                        w.write('\n')
                n = n + 1
                print(i, n)
            w.close()
        r.close()
