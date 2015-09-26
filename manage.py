import os

from flask.ext.script import Manager
from flask.ext.script.commands import ShowUrls, Clean
from flask.ext.migrate import Migrate, MigrateCommand

from app import create_app, db


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)
manager.add_command("urls", ShowUrls(order='endpoint'))
manager.add_command("clean", Clean())


if __name__ == '__main__':
    manager.run()
