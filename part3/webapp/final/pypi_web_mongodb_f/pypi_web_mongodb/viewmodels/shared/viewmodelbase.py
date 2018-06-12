from pyramid.request import Request

from pypi_web_mongodb.infrastructure import request_dict
from pypi_web_mongodb.infrastructure.user_session import UserSession


class ViewModelBase:
    def __init__(self, request: Request):
        self.request = request
        self.request_dict = request_dict.create(request)
        self.error: str = None

        self.user_svc: UserSession = UserSession(request)
        self.user = self.user_svc.user

    def to_dict(self) -> dict:
        data = dict(self.__dict__)
        del data['user_svc']
        del data['request']
        del data['request_dict']

        return self.__dict__
