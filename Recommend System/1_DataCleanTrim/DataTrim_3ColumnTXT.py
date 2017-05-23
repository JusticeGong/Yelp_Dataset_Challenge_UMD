with open('D:/Workplace/BigData/DataTrim/review_restaurant_trim.txt', 'r', encoding='utf8') as r:
    with open('D:/Workplace/BigData/DataTrim/review_restaurant_trim_remove_review.txt', 'w', encoding='utf8') as w:
        for line in r:
            line = line.split(',')
            w.write(str(line[0]) + ',' + str(line[1]) + ',' + str(line[2]) + '\n')
        w.close()
    r.close()