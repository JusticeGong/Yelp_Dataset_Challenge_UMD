import json
i = 0
with open('D:/Workplace/BigData/estimate.json', 'w', encoding="utf8") as dest_file:
    with open('D:/Workplace/BigData/yelp_academic_dataset_business_trim.json', 'r', encoding="utf8") as source_file:
        for line in source_file:
            element = json.loads(line.strip())
            dest_file.write(json.dumps(element)+"\n")
            i = i + 1
            if i >= 10000:
                break
        source_file.close()
    dest_file.close()
