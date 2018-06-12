from pyramid.request import Request
import pypi_web_mongodb.services.user_service as user_service
from pypi_web_mongodb.infrastructure import cookie_auth


class UserSession:
    def __init__(self, request: Request):
        self.request = request
        self.logged_in_id = cookie_auth.get_user_id_via_auth_cookie(request)
        self.__logged_in_user = None

    @property
    def user(self):
        if self.__logged_in_user:
            return self.__logged_in_user

        if not self.logged_in_id:
            return None

        self.__logged_in_user = user_service.user_by_id(self.logged_in_id)
        return self.__logged_in_user

    def login(self, user_id: int):
        cookie_auth.set_auth(self.request, user_id)

    def logout(self):
        cookie_auth.logout(self.request)
