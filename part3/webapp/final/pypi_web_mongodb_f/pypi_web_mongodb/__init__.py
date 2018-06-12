from pyramid.config import Configurator

# noinspection PyUnresolvedReferences
import pypi_web_mongodb
from pypi_web_mongodb.data import mongo_setup


def main(_, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    init_includes(config)
    init_routes(config)
    init_db(config)

    return config.make_wsgi_app()


def init_routes(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('help', '/help')
    config.add_route('project', '/project/{package_name}')
    config.add_route('project/', '/project/{package_name}/')

    config.add_route('releases/ver', '/project/{package_name}/releases/{release_version}')
    config.add_route('project_with_release', '/project/{package_name}/{release_version}')

    config.add_route('releases/', '/project/{package_name}/releases/')
    config.add_route('releases', '/project/{package_name}/releases')

    config.add_route('account_home', '/account')
    config.add_route('login', '/account/login')
    config.add_route('register', '/account/register')
    config.add_route('logout', '/account/logout')

    config.scan()


def init_includes(config):
    config.include('pyramid_chameleon')


def init_db(config):
    db_name = config.get_settings().get('db_name')
    mongo_setup.global_init(db_name=db_name)
