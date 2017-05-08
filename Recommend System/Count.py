import json
with open('D:/Workplace/BigData/yelp_academic_dataset_review_trim.json', 'r', encoding="utf8") as f:
    i = 0
    j = 0
    k = 0
    u = []
    b = []
    for line in f:
        element = json.loads(line.strip())
        if (str(element['user_id'])) not in u:
            i = i + 1
            u.append(str(element['user_id']))
        if (str(element['business_id'])) not in b:
            j = j + 1
            b.append(str(element['business_id']))
        k = k + 1
        print(i, j, k)
    f.close()