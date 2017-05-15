import json


def sti(s):
    return str(abs(hash(str(s))) % (10 ** 8))


i = 0
j = 0
k = 0
u = []
b = []


with open('D:/Workplace/BigData/review_userlist.txt', 'w', encoding="utf8") as dest_file:
    with open('D:/Workplace/BigData/yelp_academic_dataset_review_trim.json', 'r', encoding="utf8") as source_file:
        for line in source_file:
            element = json.loads(line.strip())
            i = i + 1
            print(i)
            if i == 2577298:
                dest_file.write(
                    sti(element['user_id']))
            else:
                dest_file.write(
                    sti(element['user_id']) + ',')

        source_file.close()
    dest_file.close()