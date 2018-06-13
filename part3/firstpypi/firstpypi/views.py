from pyramid.view import view_config

from firstpypi.data.packages import Package


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    first_10 = Package.objects().order_by('-created_date').limit(10)
    return {
        'project': 'FirstPyPI',
        'packages': first_10
            }
