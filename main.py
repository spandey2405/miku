import urllib
import requests
import datetime, time
import json
dd = 22
mm = 8
yy = 2016
hour = 7
url = "https://graph.facebook.com/v2.8/Funtimate/feed?access_token=EAACEdEose0cBALycPw6144fX5fLkkiFHQHMZBaaTUVcGJXMLFoMC0ECMPa0Ix0JaI6kKf1uhiJTaUFYa3ahnhsOhpo81H7Wy1FRkZB6pOJCeBlgcB7VQgkx67eEpGGeWEQyDwSks7nXcy1VSCn98mMJ8hCPVEgZAotLStTwpDiFvhM1bC9PCnItYRzp6q4ZD&fields=link,created_time,message&type=uploaded"
json_post_obj = dict()
count = 1
def get_fb_post(url):
    global count
    data_from_fb = requests.get(url).json()
    print data_from_fb
    for element in data_from_fb['data']:

        try:
            if "link" in element:
                if ".gif" in element['link']:
                    image_name = "/home/sid/webserver/ideathought/gifs/" + element['id'] + ".gif"
                    urllib.urlretrieve(element['link'], image_name)
                    json_file = "/home/sid/webserver/ideathought/gifinfo/json-" + str(count) + ".json"
                    with open(json_file, 'w') as outfile:
                        json.dump(element, outfile, indent=4)

                    print json_file

                    count = count + 1

        except Exception as e:
            print e
            pass

    if "paging" in data_from_fb:
        if "next" in data_from_fb["paging"]:
            next_url = data_from_fb["paging"]["next"]
            get_fb_post(next_url)
        



if __name__ == '__main__':
    get_fb_post(url)
#     publish_token = "EAACda8fWPeQBAL3e6CTdms7pWlCccJZC1OlmjMJkEykLFfZA4ZCs5CO5pIZAkppua21D18MtpToZACL6zZBvf7MZAdXKXxQfWkQULc9l37IrxzvBqL0ahGkgjDZBHDmDjYVHfHqKgkpPAgaZBQuZCzhKhyRUc2FuUwoKe6b7qSSoYgZAQZDZD"
#     import os
#     global dd, mm, yy, min_count, hour
#     hour = hour + 1
#     if hour > 22:
#         hour = 8
#         if (mm % 2 == 0 and dd < 31):
#             dd = dd + 1
#         else:
#             mm = mm + 1
#             dd = 1
#
#     t = datetime.datetime(yy, mm, dd, hour, 0)
#     # print '{}/{}/{} {}:00'.format(dd,mm,yy, hour)
#     publishing_time = str(int(time.mktime(t.timetuple())))
#     command = '''curl -i -X POST \
#      -d "url={}" \
#      -d "scheduled_publish_time={}" \
#      -d "published=false" \
#      -d "access_token={}" \
#      "https://graph.facebook.com/v2.4/275476105939521/photos/"
#     '''.format(image_link,publishing_time,publish_token)
#     os.system(command)
#
# for i in range(1,294):
#     count = 294-i
#     image_link = "http://onlinecoder.in/club-miku-images/image-{}.jpg".format(str(count))
#     pulish_post(image_link)