from flask import (
    abort,
    g,
    render_template,
)

from . import www
from .. import cache as cac

@www.route('/', methods=['GET'])
def index():
    return render_template('www/index.html')


@www.route('/cache', methods=['GET'])
def cache():
    if not cac.cache.get('counter'):
        cac.cache.set('counter', value=0)
    value = cac.cache.inc(key='counter')

    return render_template('www/cache.html', value=value)
