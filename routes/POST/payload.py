from flask_restful import Resource, reqparse
from routes.POST.X_GitHub_Events.pullrequest import PullRequest

parser = reqparse.RequestParser()

parser.add_argument('action', location='json')
parser.add_argument('X-GitHub-Event', type=str, location='headers')
parser.add_argument('X-Hub-Signature', type=str, location='headers')
parser.add_argument('X-GitHub-Delivery', type=str, location='headers')


class GithubWebhookPayload(Resource):
    def post(self):
        args = parser.parse_args()

        responseCode = 200
        responseObject = {'Event': args['X-GitHub-Event']}

        event_type = args['X-GitHub-Event']

        if event_type == 'pull_request':
            responder = PullRequest(args)
            response = responder.handle_request()
            responseCode = 200
        else:
            responseObject['Response'] = 'Event type not recognized'
            responseCode = 400

        return responseObject, responseCode
