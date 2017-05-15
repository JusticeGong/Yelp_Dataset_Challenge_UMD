index = ['00','13','25','37']
MSE = {}
MAPE = {}

for i in index:
    mses = 0
    mapes = 0
    n = 0
    j = int(i[1])
    ipath = 'D:/Workplace/BigData/DataTrim/Evaluation/MSE/ModelOutput'+i+'.txt'
    with open(ipath, 'r', encoding='utf8') as r:
        for line in r:
            line = line.strip()
            line = line.split(',')
            mses = mses + (float(line[2]) - float(line[3])) ** 2
            mapes = mapes + abs(float(line[2]) - float(line[3])) / float(line[2])
            n = n + 1
            print(i, n)
        r.close()
    MSE[str(i)] = mses / float(2577310.0)
    MAPE[str(i)] = mapes / float(2577310.0)
print(MSE)
print(MAPE)