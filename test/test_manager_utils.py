from utils.manager_utils import get_user_choice
import pytest
from unittest.mock import patch, Mock
from unittest import TestCase



class TestGetUserChoice():

    @pytest.mark.parametrize('user_input', ['l', 'e', 'r', 'd', 'x'])
    def test_function_returns_choice_for_valid_choice(self, user_input):
        with patch('builtins.input', return_value=user_input):
            result = get_user_choice()
            assert result == user_input

    @pytest.mark.parametrize('user_input', ['a', 't', '!', ' ', 'X'])
    def test_function_returns_choice_for_valid_choice(self, user_input, capsys):
        with patch('builtins.input', return_value=user_input):
            result = get_user_choice()
            captured = capsys.readouterr()
            assert captured.out == 'invalid input.\n'
            assert result == 'invalid'
            