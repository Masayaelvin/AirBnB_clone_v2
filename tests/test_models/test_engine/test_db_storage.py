#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models import storage
import os
import pytest

class Test__Init__:

    # Instantiates a DBStorage object with no errors
    def test_instantiation_no_errors(self):
        db_storage = DBStorage()
        assert isinstance(db_storage, DBStorage)

    # Sets the private attribute '__engine' to a valid SQLAlchemy engine object
    def test_sets_engine_attribute(self):
        db_storage = DBStorage()
        assert isinstance(db_storage._DBStorage__engine, create_engine)

    # Does not set the private attribute '__session'
    def test_does_not_set_session_attribute(self):
        db_storage = DBStorage()
        assert not hasattr(db_storage, '_DBStorage__session')

    # Raises an exception when HBNB_MYSQL_USER is not set
    def test_raises_exception_no_mysql_user(self):
        with pytest.raises(Exception):
            os.environ['HBNB_MYSQL_USER'] = ''
            db_storage = DBStorage()

    # Raises an exception when HBNB_MYSQL_PWD is not set
    def test_raises_exception_no_mysql_pwd(self):
        with pytest.raises(Exception):
            os.environ['HBNB_MYSQL_PWD'] = ''
            db_storage = DBStorage()

    # Raises an exception when HBNB_MYSQL_HOST is not set
    def test_raises_exception_no_mysql_host(self):
        with pytest.raises(Exception):
            os.environ['HBNB_MYSQL_HOST'] = ''
            db_storage = DBStorage()



class TestNew:

    # Given a valid object, it should be added to the current database session
    def test_valid_object_added_to_session(self):
        db_storage = DBStorage()
        obj = BaseModel()
        db_storage.new(obj)
        assert obj in db_storage._DBStorage__session

    # Given multiple valid objects, they should all be added to the current database session
    def test_multiple_valid_objects_added_to_session(self):
        db_storage = DBStorage()
        obj1 = BaseModel()
        obj2 = Amenity()
        obj3 = Place()
        db_storage.new(obj1)
        db_storage.new(obj2)
        db_storage.new(obj3)
        assert obj1 in db_storage._DBStorage__session
        assert obj2 in db_storage._DBStorage__session
        assert obj3 in db_storage._DBStorage__session

    # Given an object with no attributes, it should still be added to the current database session
    def test_object_with_no_attributes_added_to_session(self):
        db_storage = DBStorage()
        obj = BaseModel()
        db_storage.new(obj)
        assert obj in db_storage._DBStorage__session

    # Given an object with a non-existing foreign key, it should raise an error
    def test_object_with_non_existing_foreign_key_raises_error(self):
        db_storage = DBStorage()
        obj = Review()
        with pytest.raises(Exception):
            db_storage.new(obj)

    # Given an object with a non-existing attribute, it should raise an error
    def test_object_with_non_existing_attribute_raises_error(self):
        db_storage = DBStorage()
        obj = User()
        with pytest.raises(Exception):
            db_storage.new(obj)

    # Given an object with a non-existing class, it should raise an error
    def test_object_with_non_existing_class_raises_error(self):
        db_storage = DBStorage()
        obj = InvalidClass()
        with pytest.raises(Exception):
            db_storage.new(obj)

class TestSave:

    # successfully commits changes to the current database session
    def test_successfully_commits_changes(self):
        db_storage = DBStorage()
        db_storage.reload()
        obj = SomeObject()
        db_storage.new(obj)
        db_storage.save()
        assert obj in db_storage.all().values()

    # saves changes made to a single object in the current database session
    def test_saves_changes_single_object(self):
        db_storage = DBStorage()
        db_storage.reload()
        obj = SomeObject()
        db_storage.new(obj)
        obj.attribute = "new value"
        db_storage.save()
        assert obj.attribute == "new value"

    # saves changes made to multiple objects in the current database session
    def test_saves_changes_multiple_objects(self):
        db_storage = DBStorage()
        db_storage.reload()
        obj1 = SomeObject()
        obj2 = SomeObject()
        db_storage.new(obj1)
        db_storage.new(obj2)
        obj1.attribute = "new value 1"
        obj2.attribute = "new value 2"
        db_storage.save()
        assert obj1.attribute == "new value 1"
        assert obj2.attribute == "new value 2"

    # saves changes made to an object with no attributes in the current database session
    def test_saves_changes_object_no_attributes(self):
        db_storage = DBStorage()
        db_storage.reload()
        obj = SomeObject()
        db_storage.new(obj)
        db_storage.save()
        assert obj in db_storage.all().values()

    # saves changes made to an object with a null attribute in the current database session
    def test_saves_changes_object_null_attribute(self):
        db_storage = DBStorage()
        db_storage.reload()
        obj = SomeObject()
        obj.attribute = None
        db_storage.new(obj)
        obj.attribute = "new value"
        db_storage.save()
        assert obj.attribute == "new value"

    # saves changes made to an object with a large number of attributes in the current database session
    def test_saves_changes_object_large_number_attributes(self):
        db_storage = DBStorage()
        db_storage.reload()
        obj = SomeObject()
        for i in range(1000):
            setattr(obj, f"attribute{i}", f"value{i}")
        db_storage.new(obj)
        obj.attribute0 = "new value"
        db_storage.save()
        assert obj.attribute0 == "new value"



class TestDelete:

    # delete an object from the current database session
    def test_delete_object_from_session(self):
        db_storage = DBStorage()
        obj = BaseModel()
        db_storage.new(obj)
        db_storage.save()
        db_storage.delete(obj)
        assert obj not in db_storage.all().values()

    # do nothing if obj is None
    def test_do_nothing_if_obj_is_none(self):
        db_storage = DBStorage()
        obj = None
        db_storage.delete(obj)
        assert True

    # delete only the specified object
    def test_delete_only_specified_object(self):
        db_storage = DBStorage()
        obj1 = BaseModel()
        obj2 = BaseModel()
        db_storage.new(obj1)
        db_storage.new(obj2)
        db_storage.save()
        db_storage.delete(obj1)
        assert obj1 not in db_storage.all().values()
        assert obj2 in db_storage.all().values()

    # delete an object that has already been deleted
    def test_delete_already_deleted_object(self):
        db_storage = DBStorage()
        obj = BaseModel()
        db_storage.new(obj)
        db_storage.save()
        db_storage.delete(obj)
        db_storage.delete(obj)
        assert True

    # delete an object that has been deleted from the database
    def test_delete_object_deleted_from_database(self):
        db_storage = DBStorage()
        obj = BaseModel()
        db_storage.new(obj)
        db_storage.save()
        db_storage.delete(obj)
        db_storage.reload()
        assert obj not in db_storage.all().values()

    # delete an object that has not been added to the session
    def test_delete_object_not_added_to_session(self):
        db_storage = DBStorage()
        obj = BaseModel()
        db_storage.delete(obj)
        assert True



class TestReload:

    # should create all tables in the database using Base.metadata.create_all
    def test_create_all_tables(self):
        db_storage = DBStorage()
        db_storage.reload()
        assert len(Base.metadata.tables) == 7

    # should create a new session factory using sessionmaker
    def test_create_session_factory(self):
        db_storage = DBStorage()
        db_storage.reload()
        assert isinstance(db_storage._DBStorage__session, scoped_session)

    # should create a new scoped session using the session factory
    def test_create_scoped_session(self):
        db_storage = DBStorage()
        db_storage.reload()
        assert isinstance(db_storage._DBStorage__session(), scoped_session)

    # should handle errors when creating tables using Base.metadata.create_all
    def test_handle_create_all_errors(self):
        db_storage = DBStorage()
        with pytest.raises(Exception):
            db_storage.reload()

    # should handle errors when creating a new session factory using sessionmaker
    def test_handle_session_factory_errors(self):
        db_storage = DBStorage()
        with pytest.raises(Exception):
            db_storage.reload()

    # should handle errors when creating a new scoped session using the session factory
    def test_handle_scoped_session_errors(self):
        db_storage = DBStorage()
        with pytest.raises(Exception):
            db_storage.reload()




class TestClose:

    # Calling close method on an instance of DBStorage should remove the session attribute
    def test_remove_session_attribute(self):
        db_storage = DBStorage()
        db_storage.reload()
        assert hasattr(db_storage, '_DBStorage__session')
        db_storage.close()
        assert not hasattr(db_storage, '_DBStorage__session')

    # Calling close method multiple times on an instance of DBStorage should not raise any errors
    def test_multiple_close_calls(self):
        db_storage = DBStorage()
        db_storage.reload()
        assert hasattr(db_storage, '_DBStorage__session')
        db_storage.close()
        assert not hasattr(db_storage, '_DBStorage__session')
        db_storage.close()
        assert not hasattr(db_storage, '_DBStorage__session')

    # Calling close method after saving changes to the session should remove the session attribute
    def test_close_after_save(self):
        db_storage = DBStorage()
        db_storage.reload()
        assert hasattr(db_storage, '_DBStorage__session')
        obj = BaseModel()
        db_storage.new(obj)
        db_storage.save()
        assert hasattr(db_storage, '_DBStorage__session')
        db_storage.close()
        assert not hasattr(db_storage, '_DBStorage__session')

    # Calling close method on an instance of DBStorage with no session attribute should not raise any errors
    def test_close_no_session_attribute(self):
        db_storage = DBStorage()
        assert not hasattr(db_storage, '_DBStorage__session')
        db_storage.close()

    # Calling close method on an instance of DBStorage with a closed session attribute should not raise any errors
    def test_close_closed_session_attribute(self):
        db_storage = DBStorage()
        db_storage.reload()
        assert hasattr(db_storage, '_DBStorage__session')
        db_storage.close()
        assert not hasattr(db_storage, '_DBStorage__session')
        db_storage.close()

    # Calling close method on an instance of DBStorage with a None session attribute should not raise any errors
    def test_close_none_session_attribute(self):
        db_storage = DBStorage()
        db_storage._DBStorage__session = None
        assert not hasattr(db_storage, '_DBStorage__session')
        db_storage.close()