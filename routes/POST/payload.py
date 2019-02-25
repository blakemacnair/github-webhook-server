from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('action')

class GithubWebhookPayload(Resource):
    def post(self):
        args = parser.parse_args()
        action = {'action': args['action']}
        return action, 201
