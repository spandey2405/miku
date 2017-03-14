import os, json
BASE_DIR = "gifinfo/"
path, dirs, files = os.walk(BASE_DIR).next()

for file in files:
    with open(file) as data_file:
        data = json.load(data_file)
    image_name = "gifs/" + element['id'] + ".gif"
    urllib.urlretrieve(file['link'], image_name)
    print image_name
