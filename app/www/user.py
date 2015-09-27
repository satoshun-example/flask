from flask import (
    abort,
    url_for,
    request,
    render_template,
    redirect,
)

from . import www, forms
from app import db
from app.models import User


@www.route('/users', methods=['GET', 'POST'])
def users():
    users = User.query
    form = forms.RegisterUserForm(request.form)
    if form.validate_on_submit():
        user = User(name=form.name.data)
        db.session.add(user)
        db.session.commit()
    return render_template('www/users.html',
        users=users,
        form=form)


@www.route('/users/<int:user_id>', methods=['GET'])
def user(user_id):
    user = User.query.get(user_id)
    if not user:
        abort(404)

    form = forms.EditUserForm(user=user, obj=user)
    return render_template('www/user.html', user=user, form=form)


@www.route('/users/<int:user_id>', methods=['PUT', 'POST'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        abort(404, 'User NotFound')

    form = forms.EditUserForm(user=user, formdata=request.form)
    if not form.validate_on_submit():
        abort(400, 'invalid params')

    user.name = form.name.data
    db.session.commit()

    return redirect(url_for('.user', user_id=user.id))


@www.route('/users/<int:user_id>', methods=['DELETE'])
def unregister_user(user_id):
    user = User.query.get(user_id)
    if not user:
        abort(404)
    db.session.delete(user)
    db.session.commit()

    return url_for('.users')
