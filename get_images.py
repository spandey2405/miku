import os, json, urllib
BASE_DIR = "gifinfo/"
path, dirs, files = os.walk(BASE_DIR).next()

paths_gif, dirs_gid, files_gif = os.walk("gifs/").next()

for file in files:
    with open("gifinfo/" + file) as data_file:
        data = json.load(data_file)
    image_name = "gifs/" + data['id'] + ".gif"
    if (data['id'] + ".gif") not in files_gif:
        try:
            urllib.urlretrieve(data['link'], image_name)
            print image_name
        except:
            pass
    else:
        print "skipped", image_name
