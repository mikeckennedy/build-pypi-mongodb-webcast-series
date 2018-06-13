from typing import List, Optional

from pypi_web_mongodb.data.packages import Package
from pypi_web_mongodb.data.releases import Release
from pypi_web_mongodb.data.users import User


def all_packages(limit: int) -> List[Package]:
    return list(Package.objects().order_by('-created_date').limit(limit))


def latest_packages(limit: int = 10) -> List[Package]:
    latest = Release.objects() \
        .only('package_id') \
        .order_by('-created_date') \
        .limit(50)

    pids = [r.package_id for r in latest]
    return list(Package.objects(id__in=pids).limit(limit))


def package_by_name(name: str) -> Optional[Package]:
    package = Package.objects(id=name.lower().strip()).first()
    return package


# noinspection PyUnresolvedReferences
def releases_for_package(package_id: str) -> List[Release]:
    releases = Release.objects(package_id=package_id) \
        .order_by('-major_ver', '-minor_ver', '-build_ver')
    return list(releases)


def package_count():
    return Package.objects().count()


def release_count():
    return Release.objects().count()


def maintainers(package_name: str) -> List[User]:
    p = package_by_name(package_name)
    users = User.objects(id__in=p.maintainers)

    return list(users)
