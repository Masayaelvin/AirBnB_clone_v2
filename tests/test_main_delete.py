#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models import storage
import os
import pytest

class TestCodeUnderTest:

    # Verify that the 'all' method of the FileStorage class is called with the State class as argument.
    def test_all_method_called_with_state_class(self):
        fs = FileStorage()
        with patch.object(fs, 'all') as mock_all:
            code_under_test()
            mock_all.assert_called_once_with(State)

    # Verify that the number of states returned is printed to the console.
    def test_number_of_states_printed_to_console(self, capsys):
        fs = FileStorage()
        with patch.object(fs, 'all') as mock_all:
            mock_all.return_value = {'state1': State(), 'state2': State()}
            code_under_test()
            captured = capsys.readouterr()
            assert captured.out == "All States: 2\n"

    # Verify that the information of each state is printed to the console.
    def test_information_of_each_state_printed_to_console(self, capsys):
        fs = FileStorage()
        with patch.object(fs, 'all') as mock_all:
            state1 = State(name='state1', info='info1')
            state2 = State(name='state2', info='info2')
            mock_all.return_value = {'state1': state1, 'state2': state2}
            code_under_test()
            captured = capsys.readouterr()
            assert captured.out == "info1\ninfo2\n"

    # Verify that an empty dictionary is returned if there are no states.
    def test_empty_dictionary_returned_if_no_states(self):
        fs = FileStorage()
        with patch.object(fs, 'all') as mock_all:
            mock_all.return_value = {}
            result = code_under_test()
            assert result == {}

    # Verify that an exception is raised if the 'all' method of the FileStorage class raises an exception.
    def test_exception_raised_if_all_method_raises_exception(self):
        fs = FileStorage()
        with patch.object(fs, 'all') as mock_all:
            mock_all.side_effect = Exception('Error')
            with pytest.raises(Exception):
                code_under_test()

    # Verify that the correct number of states is returned if there are multiple states.
    def test_correct_number_of_states_returned_if_multiple_states(self):
        fs = FileStorage()
        with patch.object(fs, 'all') as mock_all:
            state1 = State(name='state1', info='info1')
            state2 = State(name='state2', info='info2')
            mock_all.return_value = {'state1': state1, 'state2': state2}
            result = code_under_test()
            assert len(result) == 2




class TestCodeUnderTest:

    # Creates a new State object with name "California"
    def test_creates_new_state_with_name_california(self):
        new_state = State()
        new_state.name = "California"
        fs = FileStorage()
        fs.new(new_state)
        fs.save()
        assert fs is not None
        assert new_state is not None
        assert new_state.name == "California"

    # Adds the new State object to the FileStorage instance using fs.new()
    def test_adds_new_state_to_filestorage(self):
        new_state = State()
        new_state.name = "California"
        fs = FileStorage()
        fs.new(new_state)
        fs.save()
        assert fs.new_state is not None

    # Saves the changes made to the FileStorage instance using fs.save()
    def test_saves_changes_to_filestorage(self):
        new_state = State()
        new_state.name = "California"
        fs = FileStorage()
        fs.new(new_state)
        fs.save()
        assert fs.new_state is not None

    # FileStorage instance is None
    def test_filestorage_instance_is_none(self):
        fs = FileStorage()
        assert fs is None

    # State object is None
    def test_state_object_is_none(self):
        new_state = State()
        new_state.name = "California"
        fs = FileStorage()
        fs.new(new_state)
        fs.save()
        assert new_state is None

    # State object name is None
    def test_state_object_name_is_none(self):
        new_state = State()
        new_state.name = "California"
        fs = FileStorage()
        fs.new(new_state)
        fs.save()
        assert new_state.name is None



class TestCodeUnderTest:

    # Verify that the 'all' method of the 'fs' object is called with the 'State' class as argument
    def test_all_method_called_with_state_class(self):
        fs = FileStorage()
        with patch.object(fs, 'all') as mock_all:
            code_under_test()
            mock_all.assert_called_once_with(State)

    # Verify that the length of the returned dictionary is printed
    def test_length_of_dictionary_printed(self, capsys):
        fs = FileStorage()
        with patch.object(fs, 'all') as mock_all:
            mock_all.return_value = {'state1': State(), 'state2': State()}
            code_under_test()
            captured = capsys.readouterr()
            assert captured.out == "All States: 2\n"

    # Verify that the content of the returned dictionary is printed
    def test_content_of_dictionary_printed(self, capsys):
        fs = FileStorage()
        with patch.object(fs, 'all') as mock_all:
            mock_all.return_value = {'state1': State(), 'state2': State()}
            code_under_test()
            captured = capsys.readouterr()
            assert captured.out == "All States: 2\nstate1\nstate2\n"

    # Verify that the code behaves correctly when the 'fs' object is empty
    def test_empty_fs_object(self, capsys):
        fs = FileStorage()
        with patch.object(fs, 'all') as mock_all:
            mock_all.return_value = {}
            code_under_test()
            captured = capsys.readouterr()
            assert captured.out == "All States: 0\n"

    # Verify that the code behaves correctly when the 'State' class has no instances stored in the 'fs' object
    def test_no_instances_of_state_class(self, capsys):
        fs = FileStorage()
        with patch.object(fs, 'all') as mock_all:
            mock_all.return_value = {'state1': State()}
            code_under_test()
            captured = capsys.readouterr()
            assert captured.out == "All States: 1\nstate1\n"

    # Verify that the printed length of the dictionary is correct when the 'fs' object has multiple instances of the 'State' class
    def test_multiple_instances_of_state_class(self, capsys):
        fs = FileStorage()
        with patch.object(fs, 'all') as mock_all:
            mock_all.return_value = {'state1': State(), 'state2': State(), 'state3': State()}
            code_under_test()
            captured = capsys.readouterr()
            assert captured.out == "All States: 3\nstate1\nstate2\nstate3\n"


class TestCodeUnderTest:

    # Creates a new State object with name "Nevada"
    def test_creates_new_state_with_name_nevada(self):
        code_under_test = '''
        another_state = State()
        another_state.name = "Nevada"
        fs.new(another_state)
        fs.save()
        '''
        fs = FileStorage()
        exec(code_under_test)
        assert fs.all() == {'State.' + another_state.id: another_state}

    # Adds the new State object to the FileStorage object using the 'new' method
    def test_adds_new_state_to_filestorage(self):
        code_under_test = '''
        another_state = State()
        another_state.name = "Nevada"
        fs.new(another_state)
        fs.save()
        '''
        fs = FileStorage()
        exec(code_under_test)
        assert fs.all() == {'State.' + another_state.id: another_state}

    # Saves the FileStorage object using the 'save' method
    def test_saves_filestorage(self):
        code_under_test = '''
        another_state = State()
        another_state.name = "Nevada"
        fs.new(another_state)
        fs.save()
        '''
        fs = FileStorage()
        exec(code_under_test)
        assert fs.all() == {'State.' + another_state.id: another_state}

    # FileStorage object is empty
    def test_filestorage_is_empty(self):
        code_under_test = '''
        another_state = State()
        another_state.name = "Nevada"
        fs.new(another_state)
        fs.save()
        '''
        fs = FileStorage()
        exec(code_under_test)
        assert fs.all() == {}

    # State object has no name attribute
    def test_state_has_no_name_attribute(self):
        code_under_test = '''
        another_state = State()
        another_state.name = "Nevada"
        fs.new(another_state)
        fs.save()
        '''
        fs = FileStorage()
        exec(code_under_test)
        assert not hasattr(another_state, 'name')

    # State object is not a valid instance of the State class
    def test_state_is_not_valid_instance_of_state_class(self):
        code_under_test = '''
        another_state = State()
        another_state.name = "Nevada"
        fs.new(another_state)
        fs.save()
        '''
        fs = FileStorage()
        exec(code_under_test)
        assert not isinstance(another_state, State)



class TestCodeUnderTest:

    # Verify that the 'all' method of the 'fs' object is called with the 'State' class as argument
    def test_all_method_called_with_state_class(self):
        fs = FileStorage()
        with patch.object(fs, 'all') as mock_all:
            code_under_test()
            mock_all.assert_called_once_with(State)

    # Verify that the length of the dictionary returned by the 'all' method is printed
    def test_length_of_dictionary_printed(self, capsys):
        fs = FileStorage()
        with patch.object(fs, 'all') as mock_all:
            mock_all.return_value = {'state1': State(), 'state2': State()}
            code_under_test()
            captured = capsys.readouterr()
            assert captured.out == "All States: 2\n"

    # Verify that the state objects in the dictionary returned by the 'all' method are printed
    def test_state_objects_printed(self, capsys):
        fs = FileStorage()
        with patch.object(fs, 'all') as mock_all:
            state1 = State(name='California')
            state2 = State(name='New York')
            mock_all.return_value = {'state1': state1, 'state2': state2}
            code_under_test()
            captured = capsys.readouterr()
            assert captured.out == "California\nNew York\n"

    # Verify that an empty dictionary is printed if there are no states in the file storage
    def test_empty_dictionary_printed(self, capsys):
        fs = FileStorage()
        with patch.object(fs, 'all') as mock_all:
            mock_all.return_value = {}
            code_under_test()
            captured = capsys.readouterr()
            assert captured.out == "All States: 0\n"

    # Verify that a KeyError is raised if a state key is not found in the dictionary returned by the 'all' method
    def test_key_error_raised(self):
        fs = FileStorage()
        with patch.object(fs, 'all') as mock_all:
            mock_all.return_value = {'state1': State()}
            with pytest.raises(KeyError):
                code_under_test()

    # Verify that the state objects printed have the expected format and values
    def test_state_objects_format_and_values(self, capsys):
        fs = FileStorage()
        with patch.object(fs, 'all') as mock_all:
            state1 = State(name='California')
            state2 = State(name='New York')
            mock_all.return_value = {'state1': state1, 'state2': state2}
            code_under_test()
            captured = capsys.readouterr()
            assert captured.out == "State(name='California')\nState(name='New York')\n"



class TestCodeUnderTest:

    # Verify that all_states is a dictionary containing all instances of State.
    def test_all_states_is_dictionary_containing_all_instances_of_state(self):
        fs = FileStorage()
        state1 = State()
        state2 = State()
        fs.new(state1)
        fs.new(state2)
        all_states = fs.all(State)
        assert isinstance(all_states, dict)
        assert len(all_states) == 2
        assert state1 in all_states.values()
        assert state2 in all_states.values()

    # Verify that the length of all_states.keys() is equal to the number of instances of State.
    def test_length_of_all_states_keys_is_equal_to_number_of_instances_of_state(self):
        fs = FileStorage()
        state1 = State()
        state2 = State()
        fs.new(state1)
        fs.new(state2)
        all_states = fs.all(State)
        assert len(all_states.keys()) == 2

    # Verify that the for loop iterates over all keys in all_states and prints the corresponding value.
    def test_for_loop_iterates_over_all_keys_in_all_states_and_prints_corresponding_value(self, capsys):
        fs = FileStorage()
        state1 = State()
        state2 = State()
        fs.new(state1)
        fs.new(state2)
        all_states = fs.all(State)
        code_under_test(all_states)
        captured = capsys.readouterr()
        assert captured.out == str(state1) + "\n" + str(state2) + "\n"

    # Verify that all_states is an empty dictionary when there are no instances of State.
    def test_all_states_is_empty_dictionary_when_no_instances_of_state(self):
        fs = FileStorage()
        all_states = fs.all(State)
        assert isinstance(all_states, dict)
        assert len(all_states) == 0

    # Verify that all_states only contains instances of State.
    def test_all_states_only_contains_instances_of_state(self):
        fs = FileStorage()
        state1 = State()
        fs.new(state1)
        all_states = fs.all(State)
        assert all(isinstance(state, State) for state in all_states.values())

    # Verify that the for loop does not execute when all_states is an empty dictionary.
    def test_for_loop_does_not_execute_when_all_states_is_empty_dictionary(self, capsys):
        fs = FileStorage()
        all_states = fs.all(State)
        code_under_test(all_states)
        captured = capsys.readouterr()
        assert captured.out == ""