from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app) #wrap the app in api

names = {"esra": {"age":25, "gender": "female"},
"meliha": {"age":60, "gender": "female"},
"yılmaz": {"age":83, "gender": "female"}
}
class HelloWorld(Resource): #Resource provides handle the requests like; GET, PUT etc.
    def get(self,name): #get request is sent certain url
        return names[name]
    def post(self):
        return{"data": "Posted!"}
# now register the class above as a resource
#add_resource(Resource, key)
#Resoutce is your class you want to register
#key is defining defaault url for the that class to make it accessible
api.add_resource(HelloWorld, "/hello/<string:name>")

if __name__ == "__main__":
    app.run(debug = True)

