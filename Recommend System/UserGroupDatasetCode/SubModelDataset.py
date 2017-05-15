def UGL1(a):
    if a == 1: return 0
    elif a == 2: return 1
    elif a >= 3 and a <= 5: return 2
    else: return 3
def UGL2(a):
    if a == 1: return 0
    elif a == 2: return 1
    elif a == 3: return 2
    elif a >= 4 and a <= 6: return 3
    elif a >= 7 and a <= 23: return 4
    else: return 5
def UGL3(a):
    if a == 1: return 0
    elif a == 2: return 1
    elif a == 3: return 2
    elif a == 4: return 3
    elif a >= 5 and a <= 6: return 4
    elif a >= 7 and a <= 10: return 5
    elif a >= 11 and a <= 29: return 6
    else: return 7
def UGL(a):
    r = [0,0,0]
    r[0] = UGL1(a)
    r[1] = UGL2(a)
    r[2] = UGL3(a)
    return r
n = 0
with open('D:/Workplace/BigData/DataTrim/review_restaurant_trim_usercount.txt', 'r', encoding="utf8") as r:
    for line in r:
        line = line.strip()
        a = line.split(',')
        group = UGL(int(a[4]))
        for i in range(1, 4):
            if int(group[i-1]) != 0:
                for j in range(1, int(group[i-1] + 1)):
                    path = 'D:/Workplace/BigData/DataTrim/UserGroupList/SubModelDataset' + str(i) + str(j) + '.txt'
                    with open(path, 'a', encoding="utf8") as w:
                        w.write(line + '\n')
                        w.close()
                    print(str(n) + '----' + str(i) + str(j))
        n = n + 1