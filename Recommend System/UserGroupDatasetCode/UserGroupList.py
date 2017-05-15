def UGL1(a):
    if a == 1:
        return 0
    elif a == 2:
        return 1
    elif a >= 3 and a <= 5:
        return 2
    else:
        return 3

def UGL2(a):
    if a == 1:
        return 0
    elif a == 2:
        return 1
    elif a == 3:
        return 2
    elif a >= 4 and a <= 6:
        return 3
    elif a >= 7 and a <= 23:
        return 4
    else:
        return 5

def UGL3(a):
    if a == 1:
        return 0
    elif a == 2:
        return 1
    elif a == 3:
        return 2
    elif a == 4:
        return 3
    elif a >= 5 and a <= 6:
        return 4
    elif a >= 7 and a <= 10:
        return 5
    elif a >= 11 and a <= 29:
        return 6
    else:
        return 7

def UGL(a):
    r = [0,0,0]
    r[0] = UGL1(a)
    r[1] = UGL2(a)
    r[2] = UGL3(a)
    return r

n = 0

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


#生成QueryList
# with open('D:/Workplace/BigData/DataTrim/usercount_clean.txt', 'r', encoding="utf8") as rf:
#     for line in rf:
#         a = line.split(',')
#         b = UGL(int(a[1]))
#         for i in range(1,4):
#             if b[0] != 0:
#                 path = 'D:/Workplace/BigData/DataTrim/UserGroupList/Query' + str(i) + str(b[i-1]) + '.txt'
#                 with open(path, 'a', encoding="utf8") as wf:
#                     wf.write(str(a[0]) + ',')
#                     wf.close()
#         n = n + 1
#         print(n)
#     rf.close()




#12万分组，List1(1),List2(2),List3(3,6)，List4(7,max)
#6万分组，List1(1),List2(2),List3(3),List4(4,6)，List5(7,23),List6(24,max)
#3万分组，List1(1),List2(2),List3(3),List4(4),List5(5,6), List6(7,10), List7(11,29),List8(30,max)
