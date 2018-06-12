from pyramid.view import view_config
import pyramid.httpexceptions

from pypi_web_mongodb.viewmodels.home.package_details_viewmodel import PackageDetailsViewModel


@view_config(route_name='project_with_release', renderer='pypi_web_mongodb:templates/home/package.pt')
@view_config(route_name='project', renderer='pypi_web_mongodb:templates/home/package.pt')
@view_config(route_name='project/', renderer='pypi_web_mongodb:templates/home/package.pt')
def project(request):
    vm = PackageDetailsViewModel(request)

    if vm.is_latest and vm.release_version:
        raise pyramid.httpexceptions.HTTPFound('/project/{}'.format(vm.package.id))

    return vm.to_dict()


@view_config(route_name='releases', renderer='pypi_web_mongodb:templates/home/releases.pt')
@view_config(route_name='releases/', renderer='pypi_web_mongodb:templates/home/releases.pt')
@view_config(route_name='releases/ver', renderer='pypi_web_mongodb:templates/home/releases.pt')
def releases(request):
    vm = PackageDetailsViewModel(request)
    return vm.to_dict()
