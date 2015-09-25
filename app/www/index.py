from flask import (
    abort,
    g,
    render_template,
)

from . import www

@www.route('/', methods=['GET'])
def index():
    return render_template('www/index.html')
