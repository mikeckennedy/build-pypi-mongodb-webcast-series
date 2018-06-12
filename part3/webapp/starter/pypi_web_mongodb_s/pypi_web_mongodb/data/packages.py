import datetime

import mongoengine


class Package(mongoengine.Document):
    __tablename__ = 'packages'

    id = mongoengine.StringField(primary_key=True)
    created_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    summary = mongoengine.StringField()
    description = mongoengine.StringField()

    home_page = mongoengine.StringField()
    docs_url = mongoengine.StringField()
    package_url = mongoengine.StringField()

    author = mongoengine.StringField()
    author_email = mongoengine.StringField()
    license = mongoengine.StringField()

    maintainers = mongoengine.ListField(mongoengine.ObjectIdField())

    meta = {
        'db_alias': 'core',
        'collection': 'packages',
        'indexes': [
            'created_date',
            'author_email',
            'license',
        ]
    }

    def __repr__(self):
        desc = self.description
        if desc:
            desc = desc[:50]
        return \
            """
Package {}
    created_date: {}, {}
    summary: {}, {}
    description: {}, {}
    home_page: {}, {}
    docs_url: {}, {}
    package_url: {}, {}
    author: {}, {}
    author_email: {}, {}
    license: {}, {}
""".format(
                self.id,
                type(self.created_date), self.created_date.isoformat(),
                type(self.summary), self.summary,
                type(self.description), desc,
                type(self.home_page), self.home_page,
                type(self.docs_url), self.docs_url,
                type(self.package_url), self.package_url,
                type(self.author), self.author,
                type(self.author_email), self.author_email,
                type(self.license), self.license
            )
