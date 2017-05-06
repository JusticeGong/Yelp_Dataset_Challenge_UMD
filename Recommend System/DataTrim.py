import json

with open('D:/Workplace/BigData/yelp_academic_dataset_review_trim.json', 'w', encoding="utf8") as dest_file:
    with open('D:/Workplace/BigData/yelp_academic_dataset_review - Copy.json', 'r', encoding="utf8") as source_file:
        for line in source_file:
            element = json.loads(line.strip())
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
            dest_file.write(json.dumps(element)+"\n")




