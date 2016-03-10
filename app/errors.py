from .exceptions import NotFoundException

def register_errorhandlers(app):
    @app.errorhandler(404)
    @app.errorhandler(NotFoundException)
    def not_found(e):
        return 'Not Found'

    @app.errorhandler(500)
    def server_error(e):
        return '500'
