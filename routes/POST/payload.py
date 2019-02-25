from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()

parser.add_argument('action', location='json')
parser.add_argument('X-GitHub-Event', type=str, location='headers')
parser.add_argument('X-Hub-Signature', type=str, location='headers')
parser.add_argument('X-GitHub-Delivery', type=str, location='headers')

class GithubWebhookPayload(Resource):
    def post(self):
        args = parser.parse_args()
        print(args)
        action = {'action': args['action']}
        return action, 201
