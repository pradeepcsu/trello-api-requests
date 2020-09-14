"""Positive and negative unit test cases."""
import unittest
import random
import string
from trello_util_fun import Trello_Util
from authorization import key, token
from data_variables import board_name, card_names, list_names
from trello_util_fun import Trello_Util

REPO_ROOT = pathlib.Path(__file__).parent

class TrelloRequestsTestCases(unittest.TestCase):
    """
    Unit Test Cases for testing word process
    """

    def test_add_board(self):
        """Verify the add board method"""
        # given
        test_obj = Trello_Util(key, token)

        #exercise
        #board name should be randomly given to execute the tests multiple times
        # board_name_random = ''.join(random.choices(string.ascii_uppercase, 6))
        result_flag = test_obj.add_board(board_name[0])

        #verify
        # add board request return 200 status code
        self.assertTrue(result_flag)
        board_list = test_obj.get_board_names
        # check board is successfully added to the existing boards list
        self.assertTrue(board_name[0] in board_list)

if __name__ == '__main__':
    unittest.main()
