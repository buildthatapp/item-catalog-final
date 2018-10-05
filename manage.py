from __init__ import app, db
from models import User, Item
from flask_script import Manager, prompt_bool
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def initdb():
    db.create_all()
    db.session.add(User(username="louis", email="buildthatapp@gmail.com"))
    db.session.add(User(username="test", email="example@example.com"))

    """def add_item(title, description):
        db.session.add(Item(title=title, description=description, user=magdaleno))

    for name in ["python","flask","webdev","programming","emacs", "go","golang","javascript","dev","angularjs","django","databases","orm","training"]:
        db.session.add(Tag(name=name))
    db.session.commit()

    add_item("Red Bicycle", "A new red bicycle")
    add_item("Blue Bicycle", "A used blue bicycle")

    anonymous = User(username="anonymous", email="anonymous@example.com")
    db.session.add(anonymous)"""
    db.session.commit()

    print('Database Initialized.')


@manager.command
def dropdb():
    if prompt_bool("Are you sure you want to loose all your data?"):
        db.drop_all()
        print('Dropped the database')


if __name__ == '__main__':
    manager.run()