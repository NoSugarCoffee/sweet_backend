from flask import Flask
from .config import DefaultConfig
from .extensions import db
from .extensions import migrate
from app.article.view import articles_bp
from app.space.view import space_bp


def create_app(config=None, app_name=None, blueprints=None):
    if app_name is None:
        app_name = DefaultConfig.PROJECT
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS

    app = Flask(app_name,
                instance_relative_config=True)

    configure_app(app, config)
    configure_hook(app)
    configure_blueprints(app, blueprints)
    configure_extensions(app)
    configure_logging(app)
    configure_error_handlers(app)

    return app


DEFAULT_BLUEPRINTS = [articles_bp, space_bp]


def configure_app(app, config=None):
    app.config.from_object(DefaultConfig)
    app.config.from_pyfile('production.cfg', silent=True)
    if config:
        app.config.from_object(config)


def configure_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def configure_blueprints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_logging(app):
    pass


def configure_hook(app):
    @app.before_request
    def before_request():
        pass


def configure_error_handlers(app):
    @app.errorhandler(403)
    def forbidden_page(error):
        return "Oops! You don't have permission to access this page.", 403

    @app.errorhandler(404)
    def page_not_found(error):
        return "Opps! Page not found.", 404

    @app.errorhandler(500)
    def server_error_page(error):
        return "Oops! Internal server error. Please try after sometime.", 500