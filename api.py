from flask import Flask, request
from flask_restful import Resource, Api
from flask_api import status

app = Flask(__name__)
api = Api(app)


class HelloResource(Resource):
    def get(self):
        return {"res": "estoy funcionando xD"}, 200

    def post(self):
        data = request.get_json(force=True)
        response = {
            'message': 'hello world!!!',
            'parameters': data
        }
        return response, status.HTTP_200_OK

api.add_resource(HelloResource, '/hello-world')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
