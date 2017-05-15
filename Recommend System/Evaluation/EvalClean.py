index = ['00','13','25','37']
#trim MidOutput, select 5 digits
for i in index:
    j = int(i[1])
    ipath = 'D:/Workplace/BigData/DataTrim/Evaluation/MidOutput'+i+'.txt'
    opath = 'D:/Workplace/BigData/DataTrim/Evaluation/MSE/MidOutput'+i+'.txt'
    n = 0
    with open(ipath, 'r', encoding='utf8') as r:
        with open(opath, 'w', encoding='utf8') as w:
            for line in r:
                output = []
                line = line.strip()
                line = line.replace(' ', '')
                line = line.replace('[', '')
                line = line.replace(']', '')
                line = line.replace("'", '')
                line = line.split(',')
                for k in range(3, 4 + j):
                    s = str(line[k])
                    s = s[:5]
                    line[k] = str(s)
                for p in range(0, 4 + j):
                    w.write(line[p])
                    if p != 3 + j:
                        w.write(',')
                    else:
                        w.write('\n')
                n = n + 1
                print(i, n)
            w.close()
        r.close()

# Find the best model output for MSE
# for i in index:
#     j = int(i[1])
#     ipath = 'D:/Workplace/BigData/DataTrim/Evaluation/MSE/MidOutput' + i + '.txt'
#     opath = 'D:/Workplace/BigData/DataTrim/Evaluation/MSE/ModelOutput' + i + '.txt'
#     n = 0
#     with open(ipath, 'r', encoding='utf8') as r:
#         with open(opath, 'w', encoding='utf8') as w:
#             for line in r:
#                 line = line.strip()
#                 line = line.split(',')
#                 for k in range(4, 4 + j):
#                     if float(line[k]) != 0:
#                         line[3] = line[k]
#                 for p in range(0, 4):
#                     w.write(line[p])
#                     if p != 3:
#                         w.write(',')
#                     else:
#                         w.write('\n')
#                 n = n + 1
#                 print(i, n)
#             w.close()
#         r.close()