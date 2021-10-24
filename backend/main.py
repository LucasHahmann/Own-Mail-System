# Imports
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS , cross_origin
import mail, json

# Init Flask
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)



# Class
class HelloFlask(Resource):
    def get(self):
        return {'hello': 'flask'}
    def post(self):
        print(self)

class GetEmails(Resource):
    def post(self, username, password):
        #mail.getMails(username, password)
        f = open("mail.json", "r")
        data = f.read()
        
        return json.loads(data)

# Add Routes
api.add_resource(HelloFlask, '/api/')
api.add_resource(GetEmails, '/api/getEmails/<string:username>/<string:password>')

# Start the engine
if __name__ == '__main__':
    app.run(debug=True)