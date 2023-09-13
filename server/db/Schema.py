import settings
from dataclasses import dataclass


@dataclass
class User(settings.db.Model):
    id = settings.db.Column(settings.db.Integer,
                            primary_key=True)
    name = settings.db.Column(settings.db.String(120),
                              unique=True,
                              nullable=False)
    lastname = settings.db.Column(settings.db.String(120),
                                  unique=True,
                                  nullable=False)
    email = settings.db.Column(settings.db.String(120),
                               unique=True,
                               nullable=False)
    hash = settings.db.Column(settings.db.TEXT,
                              nullable=False)

    def as_dict(self):
        return {
            "id": self.id,
            "email": self.email,
        }


@dataclass
class Admin(settings.db.Model):
    id = settings.db.Column(settings.db.Integer,
                            primary_key=True)
    name = settings.db.Column(settings.db.String(120),
                              unique=True,
                              nullable=False)
    lastname = settings.db.Column(settings.db.String(120),
                                  unique=True,
                                  nullable=False)
    email = settings.db.Column(settings.db.String(120),
                               unique=True,
                               nullable=False)
    hash = settings.db.Column(settings.db.TEXT,
                              nullable=False)

    def as_dict(self):
        return {
            "id": self.id,
            "email": self.email,
        }
