from pyramid.request import Request

from pypi_web_mongodb.services import user_service
from pypi_web_mongodb.viewmodels.shared.viewmodelbase import ViewModelBase


class LoginViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.email = self.request_dict.get('email', '').strip().lower()
        self.password = self.request_dict.get('password')

    def validate(self):
        if not self.email:
            self.error = "You must specify an email address."
        elif not self.password:
            self.error = "You must specify a password."

        self.user = user_service.login_account(self.email, self.password)
        if not self.user:
            self.error = "The user with that email and password could not be found."
