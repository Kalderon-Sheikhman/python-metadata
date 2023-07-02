import json
import os
from general_functions import run_odds_on_files, calc_odds, run_odds_on_files_id_match, append_item, \
    run_odds_on_files_id_dont_match

root_path = os.path.dirname(os.path.realpath(__file__).replace("functions", ""))
output_path = os.path.join(root_path, "output\\assets\\folder_metadata.json")
image_staging_path = os.path.join(root_path, "output\\assets\\image_staging.json")
image_metadata_path = os.path.join(root_path, "output\\assets\\image_metadata.json")

with open(output_path, 'r') as j:
    folders = json.loads(j.read())

with open("image_staging_renamed.json", 'r') as j:
    image_staging_renamed = json.loads(j.read())

with open("metadata_renamed.json", 'r') as j:
    metadata_renamed = json.loads(j.read())

folders.append(folders.pop(3))

staging_build = []
metadata_build = []

random_based_on_choice_list = ["Hatz & Hairz", "Bodz S2"]

colors = ["afb", "afm", "blank", "Bucketz", "Captain", "Cheeze", "Cowdudz", "Flippy", "Liquorice", "Stylish", "Fit",
          "Kitty", "Moon", "Plain", "Skivvyz", "Buff"]
exclude_colors = ["afb", "afm", "blank", "Bucketz", "Captain", "Cheeze", "Cowdudz", "Flippy", "Liquorice", "Stylish",
                  "Fit", "Kitty", "Moon", "Plain", "Skivvyz", "Buff"]

outputs = 1
count = 5556
while outputs <= 5555 * 2:
    if outputs <= 5555:
        staging_build.append(image_staging_renamed[outputs - 1])
        metadata_build.append(
            {"name": metadata_renamed[outputs - 1]["name"],
             "description": metadata_renamed[outputs - 1]["description"],
             "external_url": metadata_renamed[outputs - 1]["external_url"],
             "image": metadata_renamed[outputs - 1]["image"],
             "attributes": metadata_renamed[outputs - 1]["attributes"]})
        outputs += 1
    elif outputs > 5555:
        name = "Test Item #" + str(count)
        key_list, value_list, img_val_list = [], [], []
        forced_random = {"Hair Mapping": None, "Bodz Mapping": None}

        for folder in folders:
            outcome = calc_odds([True, False], [folder["rarity"], 1 - folder["rarity"]])
            if outcome:
                if folder["folder"] not in random_based_on_choice_list:
                    chosen_item = run_odds_on_files(folder)

                    if folder["folder"] == "Hair Mapping":
                        for color in colors:
                            if color in str(chosen_item):
                                forced_random["Hair Mapping"] = color

                    if folder["folder"] == "Bodz Mapping":
                        for color in colors:
                            if color in str(chosen_item):
                                forced_random["Bodz Mapping"] = color

                    append_item(key_list, folder, chosen_item, value_list, img_val_list)

            if folder["folder"] in random_based_on_choice_list:  # Assuming file is allowed to be randomly selected
                if folder["folder"] == "Hatz & Hairz":
                    if forced_random["Hair Mapping"] == "blank":
                        chosen_item = run_odds_on_files_id_dont_match(folder, exclude_colors)
                        append_item(key_list, folder, chosen_item, value_list, img_val_list)
                    else:
                        chosen_item = run_odds_on_files_id_match(folder, forced_random["Hair Mapping"])
                        append_item(key_list, folder, chosen_item, value_list, img_val_list)

                if folder["folder"] == "Bodz S2":
                    if forced_random["Bodz Mapping"] == "blank":
                        chosen_item = run_odds_on_files_id_dont_match(folder, exclude_colors)
                        append_item(key_list, folder, chosen_item, value_list, img_val_list)
                    else:
                        chosen_item = run_odds_on_files_id_match(folder, forced_random["Bodz Mapping"])
                        append_item(key_list, folder, chosen_item, value_list, img_val_list)

        if "Bodz S2" in key_list: #SECOND PART RANDOMIZATION
            # 1st find index
            i = key_list.index('Bodz S2')
            # 2nd moving the info of Bodz S2 to the correct index
            key_list.insert(3, key_list[i])
            value_list.insert(3, value_list[i])
            img_val_list.insert(3, img_val_list[i])
            # 3rd remove the repeated info
            key_list = key_list[:len(key_list) - 1]
            value_list = value_list[:len(value_list) - 1]
            img_val_list = img_val_list[:len(img_val_list) - 1]

        j = key_list.index("Chinz")
        k = key_list.index("Chin Mapping")
        if "Freddy Face" in value_list[j]:
            value_list[k] = "assets\\10b. Chin Mapping\\Freddy Face.png"
        else:
            value_list[k] = "assets\\10b. Chin Mapping\\Blank.png"
        staging_dict = dict(zip(key_list, value_list))
        metadata_dict = dict(zip(key_list, img_val_list))

        if outputs > 5555 and outputs <= 5555 + 1555:
            staging_dict.pop('Bodz S1', None)  #CHANGE EFFECT
            metadata_dict.pop('Bodz S1', None)
        elif outputs > 5555 and outputs > 5555 + 1555:
            staging_dict.pop('Bodz S2', None)
            metadata_dict.pop('Bodz S2', None)
            staging_dict.pop('Bodz Mapping', None)
            metadata_dict.pop('Bodz Mapping', None)

        stuff = []
        for key, value in staging_dict.items():
            stuff1 = {"trait_type": key, "value": value.split("\\")[2]}
            stuff.append(stuff1)

        if staging_dict not in staging_build:
            staging_build.append(staging_dict)
            metadata_build.append(
                {"name": name, "description": "lorum ipsum", "external_url": name + ".png", "image": name + ".png",
                 "attributes": stuff})
            outputs += 1
            count += 1

with open(image_staging_path, 'w', encoding='utf-8') as file:
    file.write(json.dumps(staging_build, indent=2))

with open(image_metadata_path, 'w', encoding='utf-8') as file:
    file.write(json.dumps(metadata_build, indent=2))
