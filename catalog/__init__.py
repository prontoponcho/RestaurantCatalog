from flask import Flask

app = Flask(__name__, static_url_path='', static_folder="static")

# package setup described at:
# http://flask.pocoo.org/docs/0.11/patterns/packages/xs
from catalog.views import *
