import json
import os

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
    db_name = config.get_settings().get('database_name', 'pypi_demo')
    server = config.get_settings().get('database_server', 'localhost')
    use_database_auth = config.get_settings().get('use_database_auth') == 'True'

    file = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        '..',
        'db_account.json')
    )
    user = None
    password = None
    if os.path.exists(file) and use_database_auth:
        with open(file, 'r', encoding='utf-8') as fin:
            auth_data = json.load(fin)
            user = auth_data.get('user')
            password = auth_data.get('password')

    if use_database_auth and (not user or not password):
        raise Exception("Use auth is true but no auth data in file at: {}".format(file))

    mongo_setup.global_init(db_name=db_name,
                            user=user, password=password,
                            server=server)
