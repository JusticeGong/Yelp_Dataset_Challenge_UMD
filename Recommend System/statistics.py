import json

with open('D:/Workplace/BigData/yelp_academic_dataset_review_trim.json', 'r', encoding="utf8") as f:
    uid = []
    u = 0
    bid = []
    b = 0
    r = 0
    for line in f:
        l = json.loads(line.strip())
        print(l['stars'])
        if l['user_id'] not in uid:
            u = u + 1
            uid.append(str(l['user_id']))
        if l['business_id'] not in uid:
            b = b + 1
            bid.append(str(l['business_id']))
        r = r + 1
    print(u,b,r)
    f.close()

    # with open('D:/Workplace/BigData/yelp_academic_dataset_review - Copy.json', 'r', encoding="utf8") as source_file:
    #     for line in source_file:
    #         element = json.loads(line.strip())
    #         if 'date' in element:
    #             del element['date']
    #         if 'text' in element:
    #             del element['text']
    #         if 'useful' in element:
    #             del element['useful']
    #         if 'funny' in element:
    #             del element['funny']
    #         if 'cool' in element:
    #             del element['cool']
    #         if 'type' in element:
    #             del element['type']
    #         dest_file.write(json.dumps(element)+"\n")
