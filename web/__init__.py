from flask import Flask

app = Flask("web")

from web.controllers import *
