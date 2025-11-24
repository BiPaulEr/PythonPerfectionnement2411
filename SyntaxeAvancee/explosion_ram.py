DIRECTORY = "C:/Users/PaulE/Documents/DataSet/AbstractArt"

import os 
from PIL import Image

def gen_image_from_directory(folder):
    for name in os.listdir(folder):
        if name.endswith(".jpg"):
            full_name = os.path.join(folder, name)
            image = Image.open(full_name)
            yield image

#impossible : list_image = list(gen_image_from_directory(DIRECTORY))

for index, image in enumerate(gen_image_from_directory(DIRECTORY)):
    image.save(os.path.join(DIRECTORY, "test", str(index)+".jpg"))