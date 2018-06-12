from pyramid.response import Response
from pyramid.view import view_config

from pypi_web_mongodb.viewmodels.home.home_viewmodel import HomeViewModel
from pypi_web_mongodb.viewmodels.shared.viewmodelbase import ViewModelBase


@view_config(route_name='home', renderer='pypi_web_mongodb:templates/home/index.pt')
def index(request):
    vm = HomeViewModel(request)
    return vm.to_dict()


@view_config(route_name='help', renderer='pypi_web_mongodb:templates/home/help.pt')
def help_(request):
    vm = ViewModelBase(request)
    return vm.to_dict()
