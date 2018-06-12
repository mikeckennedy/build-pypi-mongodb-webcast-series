import time

from pyramid.view import view_config

from pypi_web_mongodb.infrastructure import navigaiton
from pypi_web_mongodb.infrastructure.user_session import UserSession
from pypi_web_mongodb.services import user_service
from pypi_web_mongodb.viewmodels.account.account_home_viewmodel import AccountHomeViewModel
from pypi_web_mongodb.viewmodels.account.login_viewmodel import LoginViewModel
from pypi_web_mongodb.viewmodels.account.register_viewmodel import RegisterViewModel


# ################### INDEX #################################


@view_config(route_name='account_home',
             renderer='pypi_web_mongodb:templates/account/index.pt',
             request_method='GET')
def index(request):
    vm = AccountHomeViewModel(request)
    if not vm.user:
        navigaiton.redirect_to('/account/login')

    return vm.to_dict()


# ################### LOGIN #################################

@view_config(route_name='login',
             renderer='pypi_web_mongodb:templates/account/login.pt',
             request_method='GET')
def login_get(request):
    vm = LoginViewModel(request)
    if vm.user:
        navigaiton.redirect_to('/account')

    return vm.to_dict()


@view_config(route_name='login',
             renderer='pypi_web_mongodb:templates/account/login.pt',
             request_method='POST')
def login_post(request):
    vm = LoginViewModel(request)
    vm.validate()

    if not vm.user:
        # Haxors more slow
        time.sleep(5)

    if vm.error:
        return vm.to_dict()

    vm.user_svc.login(vm.user.id)
    navigaiton.redirect_to('/account')


# ################### REGISTRATION ############################

@view_config(route_name='register',
             renderer='pypi_web_mongodb:templates/account/register.pt',
             request_method='GET')
def register_get(request):
    vm = RegisterViewModel(request)
    if vm.user:
        navigaiton.redirect_to('/account')

    return vm.to_dict()


@view_config(route_name='register',
             renderer='pypi_web_mongodb:templates/account/register.pt',
             request_method='POST')
def register_post(request):
    vm = RegisterViewModel(request)
    vm.validate()

    if vm.error:
        return vm.to_dict()

    try:
        user = user_service.create_account(vm.full_name, vm.email, vm.password)
        vm.user_svc.login(user.id)
    except Exception as x:
        vm.error = 'Could not create your account: {}'.format(x)
        return vm.to_dict()

    navigaiton.redirect_to('/account')


# ################### LOGOUT ############################

@view_config(route_name='logout')
def logout(request):
    session = UserSession(request)
    session.logout()
    navigaiton.redirect_to('/')
