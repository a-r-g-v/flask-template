from flask import current_app
import flask.json


def secure_jsonify(*args, **kwargs):
    indent = None
    separators = (',', ':')

    if args and kwargs:
        raise TypeError('jsonify() behavior undefined when passed both args and kwargs')
    elif len(args) == 1:
        data = args[0]
    else:
        data = args or kwargs

    dumps_data = flask.json.htmlsafe_dumps(data, indent=indent, separators=separators).replace(u'+', u'\\u002b')
    return current_app.response_class((dumps_data, '\n'), mimetype='application/json')
