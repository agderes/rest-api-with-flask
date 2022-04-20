import requests
#set base url
BASE = "http://127.0.0.1:5000/"

#send a get request to the url that is base+key
response = requests.get(BASE + "hello/esra").json()
print(response)
#.json extension is added because I need this to not look like a repponse object
# and to actually be some kind of "information".
