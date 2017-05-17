import json
import re
import MySQLdb

# try:
# connection = MySQLdb.connect(
#     host='watershed.cand6uyaamhk.us-east-1.rds.amazonaws.com',
#     user='smart_city',
#     passwd='smartcity2',
#     db='yelp',
#     port=8000)

    # Next, obtain a cursor:
# cursor = connection.cursor()

    # Now we can execute SQL code via our cursor:

    # except:
    #     cursor.execute("update rec (" + str(q[0]) + ',' + str(q[1]) + ',' + str(q[2]) + ')')




n = 0
ro = 'Ratingsuserproducts=()[] '
with open('D:/Workplace/BigData/DataTrim/Demo/RandomUserGroupPred_1.txt', 'w', encoding="utf8") as w:
    with open('D:/Workplace/BigData/DataTrim/Demo/RandomUserGroupPred_25_0.txt', 'r', encoding="utf8") as r:
        for line in r:
            line = line.replace('),', '\n')
            line = line.replace(')][', '\n')
            for c in ro:
                line = line.replace(c, '')
            w.write(line)
        r.close()
    w.close()
with open('D:/Workplace/BigData/DataTrim/Demo/RandomUserGroupPred_1.txt', 'r', encoding="utf8") as r:
    with open('D:/Workplace/BigData/DataTrim/Demo/RandomUserGroupPred.txt', 'w', encoding="utf8") as w:
        for line in r:
            line = line.replace('\n', '')
            line = line.split(',')
            # cursor.execute("insert into rec value (" + str(line[0]) + ',' + str(line[1]) + ',' + str(line[2]) + ')')
            w.write('(' + str(line[0]) + ',' + str(line[1]) + ',' + str(line[2]) + '),')
            n = n + 1

            print(n)
            # if n == 1000:
            #     break
        r.close()




# finally:
#     # Don't forget to close DB connection
#     if connection:
#         connection.close()
