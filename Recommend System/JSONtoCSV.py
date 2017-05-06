import json


def sti(s):
    return str(abs(hash(str(s))))


i = 0
j = 0
k = 0
u = []
b = []

with open('D:/Workplace/BigData/yelp_academic_dataset_review_trim_long.txt', 'w', encoding="utf8") as dest_file:
    with open('D:/Workplace/BigData/yelp_academic_dataset_review_trim.json', 'r', encoding="utf8") as source_file:
        for line in source_file:
            element = json.loads(line.strip())
            dest_file.write(
                sti(element['user_id']) + ',' + sti(element['business_id']) + ',' + str(element['stars']) + ',' + sti(
                    element['review_id']) + '\n')
            i = i + 1
            print(i)

        source_file.close()
    dest_file.close()
