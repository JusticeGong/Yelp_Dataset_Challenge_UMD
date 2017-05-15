def UGL1(a):
    if a == 1:
        return 0
    elif a == 2:
        return 1
    elif a >= 3 and a <= 6:
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

with open('D:/Workplace/BigData/DataTrim/usercount_clean.txt', 'r', encoding="utf8") as rf:
    for line in rf:
        a = line.split(',')
        b = UGL(int(a[1]))
        for i in range(1,4):
            if b[0] != 0:
                for j in range(1, b[i-1]+1):
                    path = 'D:/Workplace/BigData/DataTrim/UserGroupList/List' + str(i) + str(j) + '.txt'
                    with open(path, 'a', encoding="utf8") as wf:
                        wf.write(str(a[0]) + ',')
                        wf.close()
        n = n + 1
        print(n)
    rf.close()


    # for line in f:
    #     a = line.split(',')
    #     b = UGL(int(a[1]))
    #     i = b[0]
    #     j = b[1]
    #     k = b[2]
    #     print(i,j,k)
    #     L1[i].append(1)
    #     # for j in b:
    #         # ResultList[i][j].append(str(a[0]))
    #         # i = i + 1
    #     # print(ResultList[0][0])
    # f.close()




#
#
# #12万分组，List1(1),List2(2),List3(3,6)，List4(7,max)
# with open('D:/Workplace/BigData/DataTrim/UserGroupList/Dilimitation12/List11.txt', 'w', encoding="utf8") as f11:
#     with open('D:/Workplace/BigData/DataTrim/UserGroupList/Dilimitation12/List12.txt', 'w', encoding="utf8") as f12:
#         with open('D:/Workplace/BigData/DataTrim/UserGroupList/Dilimitation12/List13.txt', 'w', encoding="utf8") as f13:
#             with open('D:/Workplace/BigData/DataTrim/UserGroupList/Dilimitation12/List14.txt', 'w', encoding="utf8") as f14:
# # 6万分组，List1(1),List2(2),List3(3),List4(4,6)，List5(7,23),List6(24,max)
#                 with open('D:/Workplace/BigData/DataTrim/UserGroupList/Dilimitation6/List21.txt', 'w', encoding="utf8") as f21:
#                     with open('D:/Workplace/BigData/DataTrim/UserGroupList/Dilimitation6/List22.txt', 'w',
#                               encoding="utf8") as f22:
#                         with open('D:/Workplace/BigData/DataTrim/UserGroupList/Dilimitation6/List23.txt', 'w',
#                                   encoding="utf8") as f23:
#                             with open('D:/Workplace/BigData/DataTrim/UserGroupList/Dilimitation6/List24.txt', 'w',
#                                       encoding="utf8") as f24:
#                                 with open('D:/Workplace/BigData/DataTrim/UserGroupList/Dilimitation6/List25.txt', 'w',
#                                           encoding="utf8") as f25:
#                                     with open('D:/Workplace/BigData/DataTrim/UserGroupList/Dilimitation6/List26.txt',
#                                               'w',
#                                               encoding="utf8") as f26:
# #3万分组，List1(1),List2(2),List3(3),List4(4),List5(5,6), List6(7,10), List7(11,29),List8(30,max)
#                                         with open('D:/Workplace/BigData/DataTrim/UserGroupList/Dilimitation3/List31.txt',
#                                               'w', encoding="utf8") as f31:
#                                             with open('D:/Workplace/BigData/DataTrim/UserGroupList/Dilimitation3/List32.txt',
#                                               'w', encoding="utf8") as f32:
#                                                 with open(
#                                                         'D:/Workplace/BigData/DataTrim/UserGroupList/Dilimitation3/List33.txt',
#                                                         'w', encoding="utf8") as f33:
#                                                     with open(
#                                                             'D:/Workplace/BigData/DataTrim/UserGroupList/Dilimitation3/List34.txt',
#                                                             'w', encoding="utf8") as f34:
#                                                         with open(
#                                                                 'D:/Workplace/BigData/DataTrim/UserGroupList/Dilimitation3/List35.txt',
#                                                                 'w', encoding="utf8") as f35:
#                                                             with open(
#                                                                     'D:/Workplace/BigData/DataTrim/UserGroupList/Dilimitation3/List36.txt',
#                                                                     'w', encoding="utf8") as f36:
#                                                                 with open(
#                                                                         'D:/Workplace/BigData/DataTrim/UserGroupList/Dilimitation3/List37.txt',
#                                                                         'w', encoding="utf8") as f37:
#                                                                     with open(
#                                                                             'D:/Workplace/BigData/DataTrim/UserGroupList/Dilimitation3/List38.txt',
#                                                                             'w', encoding="utf8") as f38:
