from typing import List, Optional

from pypi_web_mongodb.data.packages import Package
from pypi_web_mongodb.data.releases import Release
from pypi_web_mongodb.data.users import User


def all_packages(limit: int) -> List[Package]:
    # TODO: Get the packages, limit the size.
    return []


def latest_packages(limit: int = 10) -> List[Package]:
    # TODO: Get 50 most recent releases
    # TODO: Convert to a list of package IDs
    # TODO: Find packages in that list that have non trivial desc, trim set to limit.

    return []


def package_by_name(name: str) -> Optional[Package]:
    # TODO: Get single package by name (lowercase)
    return None


# noinspection PyUnresolvedReferences
def releases_for_package(package_id: str) -> List[Release]:
    # TODO: Get all releases for a given package
    # TODO: order by ('-major_ver', '-minor_ver', '-build_ver')
    return []


def package_count():
    # TODO: Return the count of packages
    return 0


def release_count():
    # TODO: Return the count of releases
    return 0


def maintainers(package_name: str) -> List[User]:
    # TODO: Find package
    # TODO: Get users from maintainers

    return []
