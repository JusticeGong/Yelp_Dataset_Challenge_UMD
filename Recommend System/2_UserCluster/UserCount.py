UserCount = {}
UserStat = {}
n = 0
with open('D:/Workplace/BigData/DataTrim/review_restaurant_trim.txt', 'r', encoding="utf8") as r:
    for line in r:
        line = line.strip()
        line = line.split(',')
        try:
            UserCount[str(line[0])] = UserCount[str(line[0])] + 1
        except:
            UserCount[str(line[0])] = 1
        print(n)
        n = n + 1

n = 0
with open('D:/Workplace/BigData/DataTrim/review_restaurant_trim.txt', 'r', encoding="utf8") as r:
    with open('D:/Workplace/BigData/DataTrim/review_restaurant_trim_usercount.txt', 'w', encoding="utf8") as w:
        for line in r:
            line = line.strip()
            a = line.split(',')
            w.write(line + ',' + str(UserCount[str(a[0])]) + '\n')
            print("##" + str(n))
            n = n + 1
        w.close()
    r.close()

for key, value in UserCount.items():
    try:
        UserStat[str(value)] = UserStat[str(value)] + 1
    except:
        UserStat[str(value)] = 1

with open('D:/Workplace/BigData/DataTrim/MidData/UserCountSum.csv', 'w', encoding="utf8") as w:
    for key, value in UserStat.items():
        w.write(str(key) + ',' + str(value) + '\n')
    w.close()