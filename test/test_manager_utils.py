from utils.manager_utils import get_user_choice
import pytest
from unittest.mock import Mock, patch

class TestGetUserChoice:
    def test_function_returns_choice_for_valid_choice(self):
        with patch.object(__builtins__, 'input', lambda: 'l'):
            assert get_user_choice() == 'list'
