# Imports
from flask import Flask
from flask_restful import Resource, Api

# Init Flask
app = Flask(__name__)
api = Api(app)

# Class
class HelloFlask(Resource):
    def get(self):
        return {'hello': 'flask'}

# Add Routes
api.add_resource(HelloFlask, '/')

# Start the engine
if __name__ == '__main__':
    app.run(debug=True)