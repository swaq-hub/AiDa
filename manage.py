import os
import unittest

from app import create_app, db
from flask.cli import FlaskGroup


app = create_app()
db.create_all(app=app)
manager = FlaskGroup(create_app=create_app)



@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    app.run()
