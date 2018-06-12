from typing import Any

from pyramid.request import Request


class RequestDictionary(dict):
    def __getattr__(self, key):
        return self[key]


def create(request: Request) -> Any:
    d = RequestDictionary({
        **request.GET,
        **request.headers,
        **request.POST,
        **request.matchdict
    })

    return d
