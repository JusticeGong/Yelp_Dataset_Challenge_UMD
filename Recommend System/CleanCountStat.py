import re

with open('D:/Workplace/BigData/DataTrim/usercount_clean.txt', 'w', encoding="utf8") as dest_f:
    with open('D:/Workplace/BigData/DataTrim/_user_gz_output_usercounts.txt_part-00000', 'r', encoding="utf8") as source_f:
        for line in source_f:
            line = re.sub('[u()]', '', line)
            line = str(line).replace("'","")
            line = line.replace(" ","")
            dest_f.write(line)
        source_f.close()
    dest_f.close()


with open('D:/Workplace/BigData/DataTrim/userstat_source.txt', 'w', encoding="utf8") as dest_f:
    with open('D:/Workplace/BigData/DataTrim/usercount_clean.txt', 'r', encoding="utf8") as source_f:
        for line in source_f:
            a = line.split(',')
            b = (a[1])
            dest_f.write(b)
        source_f.close()
    dest_f.close()

with open('D:/Workplace/BigData/DataTrim/userstat_clean.csv', 'w', encoding="utf8") as dest_f:
    with open('D:/Workplace/BigData/DataTrim/_user_gz_output_userstat.txt_part-00000', 'r',
              encoding="utf8") as source_f:
        for line in source_f:
            line = re.sub('[u()]', '', line)
            line = str(line).replace("'", "")
            line = line.replace(" ", "")
            dest_f.write(line)
        source_f.close()
    dest_f.close()