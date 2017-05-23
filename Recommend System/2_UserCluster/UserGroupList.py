import re
for i in range(1,4):
    if i == 1:
        j = 4
    elif i == 2:
        j = 6
    else:
        j = 8
    for j in range(1, j):
        n = 0
        u1 = []
        u2 = []
        path1 = 'D:/Workplace/BigData/DataTrim/UserGroupList/SubModelDataset' + str(i) + str(j) + '.txt'
        if j != 1:
            path2 = 'D:/Workplace/BigData/DataTrim/UserGroupList/SubModelDataset' + str(i) + str(j-1) + '.txt'
        else:
            path2 = 'D:/Workplace/BigData/DataTrim/review_restaurant_trim_usercount.txt'
        with open(path1, 'r', encoding='utf8') as rf1:
            for line in rf1:
                line = line.strip()
                a = line.split(',')
                u1.append(str(a[0]))
            rf1.close()
        with open(path2, 'r', encoding='utf8') as rf2:
            for line in rf2:
                line = line.strip()
                a = line.split(',')
                u2.append(str(a[0]))
            rf2.close()
        u = list(set(u1) ^ set(u2))
        path = 'D:/Workplace/BigData/DataTrim/UserGroupList/QueryList' + str(i) + str(j) + '.txt'
        with open(path, 'w', encoding='utf8') as wf:
            u = str(u)
            u = re.sub("'", '', u)
            u = u.replace('[', '')
            u = u.replace(']', '')
            wf.write(str(u))
            wf.close()
        print((i,j))


#生成UserList
# with open('D:/Workplace/BigData/DataTrim/usercount_clean.txt', 'r', encoding="utf8") as rf:
#     for line in rf:
#         a = line.split(',')
#         b = UGL(int(a[1]))
#         for i in range(1,4):
#             if b[0] != 0:
#                 for j in range(1, b[i-1]+1):
#                     path = 'D:/Workplace/BigData/DataTrim/UserGroupList/List' + str(i) + str(j) + '.txt'
#                     with open(path, 'a', encoding="utf8") as wf:
#                         wf.write(str(a[0]) + ',')
#                         wf.close()
#         n = n + 1
#         print(n)
#     rf.close()


# 生成QueryList
# with open('D:/Workplace/BigData/DataTrim/review_restaurant_trim_usercount.txt', 'r', encoding="utf8") as rf:
#     for line in rf:
#         line = line.strip()
#         a = line.split(',')
#         b = UGL(int(a[4]))
#         for i in range(1,4):
#             if b[0] != 0:
#                 path = 'D:/Workplace/BigData/DataTrim/UserGroupList/Query' + str(i) + str(b[i-1]) + '.txt'
#                 with open(path, 'a', encoding="utf8") as wf:
#                     wf.write(str(a[0]) + ',')
#                     wf.close()
#         n = n + 1
#         print(n)
#     rf.close()



