from flask_restful import Resource, reqparse


class PullRequest:

    def __init__(self, args):
        self.args = args

    def handle_request(self):
        print("handling...")
        pass
