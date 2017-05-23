import json

with open('D:/Workplace/BigData/yelp_academic_dataset_business_trim.json', 'w', encoding="utf8") as dest_file:
    with open('D:/Workplace/BigData/yelp_academic_dataset_business - Copy.json', 'r', encoding="utf8") as source_file:
        for line in source_file:
            element = json.loads(line.strip())
            if 'Restaurants' in str(element["categories"]):
                if 'is_open' in element:
                    del element['is_open']
                if 'hours' in element:
                    del element['hours']
                if 'neighborhood' in element:
                    del element['neighborhood']
                # if 'funny' in element:
                #     del element['funny']
                # if 'cool' in element:
                #     del element['cool']
                if 'type' in element:
                    del element['type']
                dest_file.write(json.dumps(element)+"\n")