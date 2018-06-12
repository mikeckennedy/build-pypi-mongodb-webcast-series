from typing import List, Optional

from pypi_web_mongodb.data.packages import Package
from pypi_web_mongodb.data.releases import Release
from pypi_web_mongodb.data.users import User


def all_packages(limit: int) -> List[Package]:
    return list(Package.objects().limit(limit))


def latest_packages(limit: int = 10) -> List[Package]:
    latest_releases = Release.objects().only('package_id').order_by('-created_date').limit(50)
    package_ids = [r.package_id for r in latest_releases]

    return [p
            for p in Package.objects().filter(id__in=package_ids)
            if p.description and len(p.description) > 100
            ][:limit]


def package_by_name(name: str) -> Optional[Package]:
    if not name:
        return None

    return Package.objects().filter(id=name.lower()).first()


# noinspection PyUnresolvedReferences
def releases_for_package(package_id: str) -> List[Release]:
    releases = list(Release.objects()
                    .filter(package_id=package_id)
                    .order_by('-major_ver', '-minor_ver', '-build_ver'))

    return releases


def package_count():
    return Package.objects().count()


def release_count():
    return Release.objects().count()


def maintainers(package_name: str) -> List[User]:
    p = Package.objects(id=package_name).first()
    if not p:
        return []

    users = list(User.objects(id__in=p.maintainers))
    return users
