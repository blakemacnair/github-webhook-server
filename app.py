#!flask/bin/python
from flask import Flask
from flask_restful import Api
from flask_restful import reqparse
from routes.GET.helloworld import HelloWorld
from routes.POST.payload import GithubWebhookPayload


app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/')

api.add_resource(GithubWebhookPayload, '/payload')

if __name__ == '__main__':
    app.run(debug=True)
