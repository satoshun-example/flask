# Flask Example

[flask](https://github.com/mitsuhiko/flask) is WEB flaskwork of Python.


## Features

- Use Python3.5
- Use SQLAlchemy
- Use Redis()
- Use Memcached


## Usage

Install

```shell
$ pip install -r requirements.txt
```

```shell
$ python manage.py
python manage.py                                                                                                                                                                ⏎
usage: manage.py [-?] {urls,clean,shell,runserver} ...

positional arguments:
  {urls,clean,shell,runserver}
    urls                Displays all of the url matching routes for the
                        project
    clean               Remove *.pyc and *.pyo files recursively starting at
                        current directory
    shell               Runs a Python shell inside Flask application context.
    runserver           Runs the Flask development server i.e. app.run()
```

Run a server.

```shell
$ python manage.py runserver
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
```

In addition to it, I'm using a [Virtualenv](https://virtualenv.pypa.io/en/latest/). Virtualenv is a tool to create isolated Python enviroments.


### Usage: DB migration

Create database on MySQL

```shell
mysql> CREATE DATABASE flasksample DEFAULT CHARACTER SET UTF8 COLLATE UTF8_GENERAL_CI;
mysql> CREATE USER 'developer'@'localhost';
mysql> GRANT ALL PRIVILEGES ON flasksample.* TO 'developer'@'%' WITH GRANT OPTION;
```

Create migration file

```shell
$ python manage.py db init
$ python manage.py db revision
  Generating /Users/satouhayabusa/git/github.com/satoshun-example/flask/migrations/versions/3973f14f923_.py ... done
```

Update DB by migration file

```shell
$ vi /Users/satouhayabusa/git/github.com/satoshun-example/flask/migrations/versions/3973f14f923_.py # edit
$ python manage.py db upgrade head                                                                                                                                                ⏎
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 3973f14f923, empty message

$ mysql -udeveloper flasksample

mysql> show tables;
+-----------------------+
| Tables_in_flasksample |
+-----------------------+
| alembic_version       |
| users                 |
+-----------------------+
2 rows in set (0.00 sec)

mysql> desc users;
+------------+--------------+------+-----+---------+----------------+
| Field      | Type         | Null | Key | Default | Extra          |
+------------+--------------+------+-----+---------+----------------+
| id         | int(11)      | NO   | PRI | NULL    | auto_increment |
| name       | varchar(255) | NO   | UNI | NULL    |                |
| created_at | datetime     | NO   |     | NULL    |                |
| updated_at | datetime     | NO   |     | NULL    |                |
+------------+--------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)
```

