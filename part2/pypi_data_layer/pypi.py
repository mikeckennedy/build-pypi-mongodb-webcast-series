import datetime

import bson

import data.mongo_setup as mongo_setup
from data.package import Package
from data.releases import Release
from data.users import User


def main():
    mongo_setup.global_init()

    add_fake_data()
    do_some_queries()


def do_some_queries():
    print("{:,} projects | {:,} releases | {:,} users".format(
        Package.objects().count(),
        Release.objects().count(),
        User.objects().count()
    ))

    name = input("Enter a package name: ").strip().lower()
    # p = Package.objects(author='hfpython').first()

    t0 = datetime.datetime.now()
    p = list(Package.objects(author_email=name))[0]
    dt = datetime.datetime.now() - t0
    print("Time elapsed: {:,} ms".format(dt.total_seconds()*1000))
    print(p.id)


    # p = Package.objects(languages__name='Legacy Python').first()
    if not p:
        print("Sorry no package like that!")
        return

    # print()
    # print("Name: " + p.id)
    # print("Summary: " + p.summary)
    # print("Description: " + p.description)


def add_fake_data():
    p = Package.objects(id='package773').first()
    if p:
        print("Already found the package {}".format(p.summary))
        return

    p = Package()

    p.id = 'package773'
    p.description = "test package"
    p.summary = "a test"
    p.license = "MIT"

    p.languages.append('Python 3.7')
    p.languages.append('Python 3.6')
    p.languages.append('Legacy Python')

    p.maintainers.append(bson.ObjectId())
    p.maintainers.append(bson.ObjectId())

    p.save()
    print("Wrote some data.")


if __name__ == '__main__':
    main()
