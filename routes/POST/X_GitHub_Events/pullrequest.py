from flask_restful import Resource, reqparse


class PullRequest:

    def __init__(self, args):
        self.args = args

    def handle_request(self):
        pr = self.args['pull_request']
        title = pr['title']
        state = pr['state']
        merged = pr['merged']
        return {'title': title, 'state': state, 'merged': merged}
