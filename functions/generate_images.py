from PIL import Image
import os
import json

root_path = os.path.dirname(os.path.realpath(__file__).replace("functions", ""))
image_gen_path = os.path.join(root_path, "output\\assets\\image_staging.json")
image_output_path = os.path.join(root_path, "output\\images\\")

with open(image_gen_path, 'r') as j:
    images_to_create = json.loads(j.read())


def paste_overlay(base_image, overlay):
    base_image = base_image.paste(overlay, (0, 0), overlay)

    return base_image

number = 1
for image in images_to_create:
    base_image = Image.new('RGB', (2500, 2500))
    for k, v in image.items():
        path = os.path.join(root_path, v)
        overlay = Image.open(path).convert("RGBA")
        paste_overlay(base_image, overlay)
    base_image.save(image_output_path + str(number) + ".png")
    number += 1