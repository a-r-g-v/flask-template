#!/usr/bin/env python
import os
from flask_script import Manager, Shell
from app import create_app
from flask import url_for


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell():
    return dict(app=app)

manager.add_command("shell", Shell(make_context=make_shell))


def run_test(discover_name):
    import unittest
    tests = unittest.TestLoader().discover(discover_name)
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def test():
    run_test('tests')


@manager.command
def list_routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print line



if __name__ == '__main__':
    manager.run()

