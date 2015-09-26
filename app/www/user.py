from flask import (
    abort,
    g,
    render_template,
)

from . import www
from app.models import User


@www.route('/users', methods=['GET'])
def users():
    users = User.query
    return render_template('www/users.html', users=users)
