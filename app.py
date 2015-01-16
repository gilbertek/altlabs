import os
import sys
import markdown
import yaml
import collections

from flask import Flask
from flask import render_template
from flask import Markup
from flask import url_for
from flask import abort
from flask import request
from flask.ext.frozen import Freezer
from werkzeug import cached_property
from werkzeug.contrib.atom import AtomFeed


POST_FILE_EXTENSION   = '.md'
POST_FILES_DIR        = 'posts'
SECRET_KEY            = 'not-so-secret'
FREEZER_BASE_URL      = 'http://localhost'
FREEZER_IGNORED_FILES = ['.git', 'CNAME', 'bower_components', 'node_modules']


app     = Flask(__name__)
app.config.from_object(__name__)
freezer = Freezer(app)

app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
