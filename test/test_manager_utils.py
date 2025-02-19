from utils.manager_utils import get_user_choice
import pytest
from unittest.mock import patch, Mock
from unittest import TestCase



class TestGetUserChoice(TestCase):

    @patch('utils.manager_utils.get_user_choice.user_choice', 'l')
    def test_function_returns_choice_for_valid_choice(self):
            result = get_user_choice()
            self.assertEqual(result, 'l')
