import data.mongo_setup as mongo_setup
from data.package import Package


def main():
    mongo_setup.global_init()

    add_fake_data()




def add_fake_data():

    p = Package.objects(id='package772').first()
    if p:
        print("Already found the package {}".format(p.summary))
        return

    p = Package()

    p.id = 'package772'
    p.description = "test package"
    p.summary = "a test"
    p.license = "MIT"

    p.save()
    print("Wrote some data.")


if __name__ == '__main__':
    main()
