import os, json
BASE_DIR = "gifinfo/"
path, dirs, files = os.walk(BASE_DIR).next()

for file in files:
    with open("gifinfo/" + file) as data_file:
        data = json.load(data_file)
    image_name = "gifs/" + data['id'] + ".gif"
    urllib.urlretrieve(data['link'], image_name)
    print image_name
