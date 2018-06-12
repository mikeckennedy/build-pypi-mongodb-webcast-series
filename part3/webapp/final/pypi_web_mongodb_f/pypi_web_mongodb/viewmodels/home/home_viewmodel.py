from pyramid.request import Request

import pypi_web_mongodb.services.package_service as package_service
import pypi_web_mongodb.services.user_service as user_service
from pypi_web_mongodb.viewmodels.shared.viewmodelbase import ViewModelBase


class HomeViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.package_count = package_service.package_count()
        self.release_count = package_service.release_count()
        self.user_count = user_service.user_count()
        self.packages = package_service.latest_packages(limit=10)
