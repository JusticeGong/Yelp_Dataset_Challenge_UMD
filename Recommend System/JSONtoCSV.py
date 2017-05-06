import json

with open('D:/Workplace/BigData/yelp_academic_dataset_review_trim.txt', 'w', encoding="utf8") as dest_file:
    with open('D:/Workplace/BigData/yelp_academic_dataset_review_trim.json', 'r', encoding="utf8") as source_file:
        # dest_file.write('user_id,business_id,stars,review_id\n')
        for line in source_file:
            element = json.loads(line.strip())
            dest_file.write(element['user_id']+','+element['business_id']+','+ str(element['stars'])+','+element['review_id']+'\n')
        source_file.close()
    dest_file.close()

        # for line in source_file:
        #     element = json.loads(line.strip())
        #     if 'date' in element:
        #         del element['date']
        #     if 'text' in element:
        #         del element['text']
        #     if 'useful' in element:
        #         del element['useful']
        #     if 'funny' in element:
        #         del element['funny']
        #     if 'cool' in element:
        #         del element['cool']
        #     if 'type' in element:
        #         del element['type']
        #     dest_file.write(json.dumps(element))