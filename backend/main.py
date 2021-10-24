# Imports
from flask import Flask
from flask_restful import Resource, Api

import mail

# Init Flask
app = Flask(__name__)
api = Api(app)

# Class
class HelloFlask(Resource):
    def get(self):
        return {'hello': 'flask'}
    def post(self):
        print(self)

class GetEmails(Resource):
    def post(self, username, password):
        mail.getMails(username, password)
        f = open("mail.json", "r")
        data = f.read()
        return data

# Add Routes
api.add_resource(HelloFlask, '/')
api.add_resource(GetEmails, '/getEmails/<string:username>/<string:password>')

# Start the engine
if __name__ == '__main__':
    app.run(debug=True)