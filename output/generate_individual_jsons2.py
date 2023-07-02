import csv
from email.mime import image
import os
import json

root_path = os.path.dirname(os.path.realpath(__file__).replace("output", ""))
input_metadata_path = os.path.join(root_path, "output\\assets\\image_metadata.json")
output_metadata_path = os.path.join(root_path, "output\\metadata_renamed.json")
csv_path = os.path.join(root_path, "output\\trait_rename.csv")

NAME = "Melted Dudz #"
DESCRIPTION = "In an attempt to bring Dudelz to life, something went horribly wrong. What emerged were melting monstrosities, and their warped and oozing bodies are a testament to the dangers of tampering with the unknown."
EXTERNAL_URL = "www.dudelz.com/melted-dudz"
FILE_EXTENSION = "ipfs://QmU4pSj3JQKZbo1xUaQKrXL1KvWkvvUvZuybcoJSHEV5Xb/"

with open(input_metadata_path, 'r') as j:
    metadata = json.loads(j.read())

rename_dict, count = [], 0
with open(csv_path, newline='') as csvfile:
    rename_file = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in rename_file:
        if count > 0:
            data = {"filename": row[0], "folder": row[1], "type1": row[2], "name1": row[3]}
            rename_dict.append(data)
        count += 1

metadata_full_dict = []
image_no = 1
for item in metadata:
    attribute_dict = []
    for attribute in item["attributes"]:
        type_ = attribute["trait_type"]
        value_ = attribute["value"]

        for file in rename_dict:
            if file["filename"] == value_ and file["folder"] == type_:
                type_n = file["type1"]
                value_n = file["name1"]

                attribute_ = {"trait_type": type_n, "value": value_n}
                attribute_dict.append(attribute_)


    #Removing Background Shapes, Hair Mapping and the ones which are empty
    new_dict=[]
    removables = ('Bodz Behind Mapping', 'Chin Mapping', 'Hair Mapping', 'Bodz Mapping', "", " ")

    for item in attribute_dict:
        x = item["trait_type"]
        if x not in removables:
            new_dict.append(item)


    item_metadata = {"name": NAME + str(image_no), "description": DESCRIPTION, "external_url": EXTERNAL_URL, "image": FILE_EXTENSION + str(image_no) + ".png",
                     "attributes": new_dict}
    metadata_full_dict.append(item_metadata)
    path = os.path.join(root_path, "output\\metadata\\" + str(image_no) + ".json")

    with open(path, 'w', encoding='utf-8') as file:
        file.write(json.dumps(item_metadata, indent=2))

    image_no += 1

with open(output_metadata_path, 'w', encoding='utf-8') as file:
    file.write(json.dumps(metadata_full_dict, indent=2))
