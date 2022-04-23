from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app) #wrap the app in api
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/esra/Desktop/rest-api-with-flask/database.db'
db = SQLAlchemy(app) 


class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable = False)
    likes = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return str.format("Video(name = {name}, views = {views}, likes={likes}")
#db.create_all() Once initialized the databse we dont need to use this command

video_put_args = reqparse.RequestParser() #automatically parsse through the request that's being send

video_put_args.add_argument("name", type = str, help="name of the video is required", required=True) #help using for what we should dispaly to the sender  if they dont send us this name argument, like error message,
video_put_args.add_argument("views", type = int, help="views of the video is required", required=True) #by adding required=True we say that you must parse this information, otherwise it'll be crashed
video_put_args.add_argument("likes", type = int, help="likes on the video is required", required=True) #if we don't require this information, this info will how up with "none" and not crashed

video_update_args = reqparse.RequestParser()

video_update_args.add_argument("name", type = str, help="name of the video is required") 
video_update_args.add_argument("views", type = int, help="views of the video is required") 
video_update_args.add_argument("likes", type = int, help="likes on the video is required") 

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'like':fields.Integer
}

class Video(Resource): #Resource provides handle the requests like; GET, PUT etc.
    @marshal_with(resource_fields)
    def get(self,video_id): #get request is sent certain url
        result = VideoModel.query.filter_by(id = video_id).first()
        if not result:
            abort(404,message="Not Found...")
        return result

    @marshal_with(resource_fields) # we cannot just return object, we need to serialize them so that we need this decorator
    def put(self,video_id):
        args = video_put_args.parse_args() # we can give code to the sender, here 201 stands for  "created", so user will know the video created successfuly, everything working fine
        result=VideoModel.query.filter_by(id = video_id)
        if result:
            abort(409, message="Video id taken...")
        video = VideoModel(id=video_id, name = args['name'], views =args['views'], likes = args['likes'])
        db.session.add(video) #temporary adding the video
        db.session.commit() #permanently putting the video
        return video, 201

    @marshal_with(resource_fields)
    def patch(self, video_id):
        args=video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id)
        if not result:
            abort(404, message="Video does not exist, cannot update")

        if args['name']:
            result.name= args['name']
        if args['views']:
            result.views= args['views']
        if args['likes']:
            result.likes= args['likes']
        
        db.session.commit()

        return result
    
    @marshal_with(resource_fields)
    def delete(self,video_id):
        result = VideoModel.query.filter_by(id = video_id)
        if not result:
            abort(404, message="Video does not exist!")
        db.session.delete(result)
        db.session.commit()
        return result

  

# now register the class above as a resource
#add_resource(Resource, key)
#Resource is your class you want to register
#key is defining defaault url for the that class to make it accessible
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug = True)

