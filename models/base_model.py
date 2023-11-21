#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
# import datetime
from datetime import datetime
from models import storage
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

if storage == "db":
    Base = declarative_base()
else:
    Base = object

class BaseModel:
    """The BaseModel class from which future classes will be derived"""
    if storage == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)


    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        if kwargs and kwargs is not None:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value =datetime.\
                        strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)

        if "id" not in kwargs.keys():
            self.id = str(uuid.uuid4())
        if "created_at" not in kwargs.keys():
            self.created_at = datetime.now()
        if "updated_at" not in kwargs.keys():
            self.updated_at = datetime.now()
        

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
    
    def delete(self):
        """delete the current instance from the storage"""
        storage.delete(self)
