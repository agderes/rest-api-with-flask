from email.mime import application
import requests
#set base url
BASE = "http://127.0.0.1:5000/"

data=[{"likes":10,"views": 4,"name": "video1435"},
{"likes":54389,"views": 985742,"name": "video1434"},
{"likes":3985,"views": 9483,"name": "video1433"},
{"likes":678,"views": 86124,"name": "video1432"}]

#send a get request to the url that is base+key
# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i]).json()
#     print(response)
# input()
# response = requests.get(BASE + "video/0").json()
# print(response)
# input()
response = requests.patch(BASE + "video/2", {"name":"video_2"}).json()
print(response)
#.json extension is added because I need this to not look like a repponse object
# and to actually be some kind of "information".
