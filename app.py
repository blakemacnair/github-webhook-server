#!flask/bin/python
from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('action')

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

class GithubWebhookPayload(Resource):
    def post(self):
        args = parser.parse_args()
        action = {'action': args['action']}
        return action, 201

api.add_resource(GithubWebhookPayload, '/payload')

if __name__ == '__main__':
    app.run(debug=True)
