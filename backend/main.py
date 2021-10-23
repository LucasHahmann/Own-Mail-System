# Imports.....
import falcon
from wsgiref.simple_server import make_server

# Global Variables

PORT = 300

# Classes from Routes
class ThingsResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = falcon.MEDIA_TEXT  # Default is JSON, so override
        resp.text = ('Hello, World!')
    def on_post(self, req, resp):
        print(req)


# Init Falcon
app = falcon.App()

# Configure class
things = ThingsResource()

# Configure Routes
app.add_route('/things', things)

if __name__ == '__main__':
    with make_server('', PORT, app) as httpd:
        print(f'Serving on port {PORT}...')

        # Serve until process is killed
        httpd.serve_forever()