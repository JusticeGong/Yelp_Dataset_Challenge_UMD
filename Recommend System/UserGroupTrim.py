UGLDict = {}

for i in range(1,4):
    if i == 1:
        for j in range(1,5):
            index = str(i) + str(j)
            # print(i, j, index)
            path = 'D:/Workplace/BigData/DataTrim/UserGroupList/List' + index + '.txt'
            with open(path, 'r', encoding="utf8") as rf:
                for line in rf:
                    a = line.split(',')
                    UGLDict[str(index)] = a

            #     rf.close()

print(UGLDict['14'])