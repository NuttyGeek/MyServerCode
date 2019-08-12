from flask import Flask
from flask_restful import Api
from server_app.resources import Hello, Ping, Upload, Keywords, SpeechToText
app = Flask(__name__)
api = Api(app, prefix='/GeoVideoApplication/')


# adding resources
api.add_resource(Hello, "/")
api.add_resource(Ping, "ping")
api.add_resource(Upload, "upload")
api.add_resource(Keywords, "keywords")
api.add_resource(SpeechToText, "test")

if __name__ == '__main__':
    app.run(debug=True)