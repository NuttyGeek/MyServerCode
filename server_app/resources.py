from flask import request
from flask_restful import Resource
from server_app.helper import get_random_name, filter_sentence, print_it
from werkzeug.utils import secure_filename
import os


class Hello(Resource):
    def get(self):
        return {"name": get_random_name()}

class Ping(Resource):
    def get(self):
        return  {"status": "Working"}


UPLOAD_FOLDER = '/tmp/uploadFolder' #os.path.join("F:", "uploadFolder")
class Upload(Resource):
    def post(self):
        file = request.files['image']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return {"message": True}


class Keywords(Resource):
    def post(self):
        args = request.get_json()
        sentence = args['sentence']
        keywords = filter_sentence(sentence)
        return {'keywords': keywords}

class SpeechToText(Resource):
    def post(self):
        args = request.args
        files = args['files']
        response_final = print_it(files)
        return response_final
