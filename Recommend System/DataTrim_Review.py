import json

u = []
i = 0
j = 0
with open('D:/Workplace/BigData/yelp_academic_dataset_business_trim.json', 'r', encoding="utf8") as f:
    for line in f:
        element = json.loads(line.strip())
        if (str(element['business_id'])) not in u:
            u.append(str(element['business_id']))
        i = i + 1
        print('#############'+ str(i))
    f.close()


with open('D:/Workplace/BigData/yelp_academic_dataset_review_trim.json', 'w', encoding="utf8") as dest_file:
    with open('D:/Workplace/BigData/yelp_academic_dataset_review - Copy.json', 'r', encoding="utf8") as source_file:
        for line in source_file:
            element = json.loads(line.strip())
            if str(element['business_id']) in u:
                if 'date' in element:
                    del element['date']
                if 'hours' in element:
                    del element['hours']
                if 'useful' in element:
                    del element['useful']
                if 'funny' in element:
                    del element['funny']
                if 'cool' in element:
                    del element['cool']
                if 'type' in element:
                    del element['type']
                if 'text' in element:
                    del element['text']
                dest_file.write(json.dumps(element)+"\n")
                j = j + 1
                print('-------------' + str(j))




