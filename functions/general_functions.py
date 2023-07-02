import numpy as np


def calc_odds(options, odds):
    choice = np.random.choice(options, 1, p=odds)

    return choice


def normalise_odds(odds):
    norm = [float(i) / sum(odds) for i in odds]

    return norm


def run_odds_on_files(folder, ):
    choices, odds = [], []
    for file in folder["files"]:
        choices.append(file["path"] + "\\" + file["file_name"])
        odds.append(file["rarity_factor"])

    if odds:
        norm = normalise_odds(odds)
        chosen_item = calc_odds(choices, norm)

    return chosen_item


def run_odds_on_files_id_match(folder, id):
    choices, odds, chosen_item = [], [], ""
    for file in folder["files"]:
        #print(file, id)
        if id in str(file):
            choices.append(file["path"] + "\\" + file["file_name"])
            odds.append(file["rarity_factor"])
    norm = normalise_odds(odds)
    chosen_item = calc_odds(choices, norm)

    return chosen_item

def run_odds_on_files_id_dont_match(folder, color_list):
    choices, odds = [], []
    for file in folder["files"]:
        if any(ext in str(file) for ext in color_list):
            a = True
        else:
            choices.append(file["path"] + "\\" + file["file_name"])
            odds.append(file["rarity_factor"])
    norm = normalise_odds(odds)
    chosen_item = calc_odds(choices, norm)

    return chosen_item


def append_item(key_list, folder, chosen_item, value_list, img_val_list):
    key_list.append(folder["folder"])
    value = chosen_item[0].split("\\")[-1]

    if "%" in value:
        value = value.split("%")[0]
    else:
        value = value.split(".png")[0]
    value_list.append(chosen_item[0])
    img_val_list.append(value)
