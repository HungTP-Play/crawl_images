# -*- encoding: utf-8 -*-
#
from class_name import class_names
from urllib.parse import quote
import os

OUT_PATH = "output"

if not os.path.exists(OUT_PATH):
    os.mkdir(OUT_PATH)

for name in class_names:
    image_sub_dir = OUT_PATH + "/" + name
    if not os.path.exists(image_sub_dir):
        os.mkdir(image_sub_dir)
    search_key = "BMW " + " ".join(name.split("-"))
    urlKeyword = quote(search_key)
    print(urlKeyword)
