from . import main


@main.app_errorhandler(404)
def not_found(e):
    return '404'


@main.app_errorhandler(500)
def server_error(e):
    return '500'
