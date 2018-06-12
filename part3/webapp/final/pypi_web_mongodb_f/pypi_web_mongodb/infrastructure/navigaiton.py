import pyramid.httpexceptions as x


def redirect_to(url, permanent=False):
    if not permanent:
        raise x.HTTPFound(location=url)
    else:
        raise x.HTTPMovedPermanently(location=url)
