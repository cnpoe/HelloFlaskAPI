from flask import Flask, request
from flask_restful import Resource, Api
from flask_api import status
import requests


app = Flask(__name__)
api = Api(app)


class HelloResource(Resource):

    def post(self):
        data = request.get_json(force=True)
        message = ""
        response_ = requests.get('http://192.241.215.103:8889/').json()
        message += response_["res"] + ' '
        response_ = requests.get('http://192.241.215.103:8888/').json()
        message += response_["res"]
        response = {
            'message': f'{message}!!!',
            'parameters': data
        }
        return response, status.HTTP_200_OK

api.add_resource(HelloResource, '/hello-world')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
