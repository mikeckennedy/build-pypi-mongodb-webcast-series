import pyramid.httpexceptions
from pyramid.request import Request

import pypi_web_mongodb.services.package_service as package_service
import pypi_web_mongodb.services.user_service as user_service

# noinspection PyPackageRequirements
import gravatar

from pypi_web_mongodb.viewmodels.shared.viewmodelbase import ViewModelBase

user_to_image_lookup = {}


class PackageDetailsViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        package_name = self.request_dict.get('package_name')
        self.release_version = self.request_dict.get('release_version')

        self.package = package_service.package_by_name(package_name)
        if not self.package:
            raise pyramid.httpexceptions.HTTPNotFound()

        self.releases = package_service.releases_for_package(self.package.id)
        self.latest_version = '0.0.0'
        self.latest_release = None
        if self.releases:
            self.latest_release = self.releases[0]
            self.latest_version = self.latest_release.version_text

        self.is_latest = not self.release_version or self.latest_version == self.release_version

        self.maintainers = package_service.maintainers(package_name)
        # print("Maintainers: {}".format(self.maintainers))
        if not self.maintainers and self.package.author_email and self.package.author_email != 'unknown':
            author = user_service.user_by_email(self.package.author_email)
            if author:
                self.maintainers = [author]
            # print("Fall back maintainers: {}".format([m.email for m in self.maintainers]))

        for m in self.maintainers:
            m.profile_image_url = self.get_image(m.email)

    @staticmethod
    def get_image(email: str) -> str:
        global user_to_image_lookup
        if email in user_to_image_lookup:
            return user_to_image_lookup.get(email)

        g = gravatar.Gravatar(email)
        user_to_image_lookup[email] = g.thumb
        return user_to_image_lookup[email]
