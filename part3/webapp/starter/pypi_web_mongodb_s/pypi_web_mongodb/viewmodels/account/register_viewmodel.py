from pyramid.request import Request

from pypi_web_mongodb.services import user_service
from pypi_web_mongodb.viewmodels.shared.viewmodelbase import ViewModelBase


class RegisterViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.first_name = self.request_dict.get('first_name', '').strip()
        self.last_name = self.request_dict.get('last_name', '').strip()
        self.email = self.request_dict.get('email', '').strip().lower()
        self.password = self.request_dict.get('password')
        self.full_name = self.first_name + ' ' + self.last_name

    def validate(self):
        if not self.first_name or not self.last_name:
            self.error = "You must specify your name."
        if not self.email:
            self.error = "You must specify an email address."
        elif not self.password:
            self.error = "You must specify a password."

        if user_service.user_by_email(self.email):
            self.error = "The user with that email already exists."
