from flask import Flask
from flask_cors import CORS

app = Flask(__name__)


from toxic import routes