from api import create_path
import unittest


class TestCreatePath(unittest.TestCase):

    def test_create_path(self):
        self.assertEqual(create_path('345'), 200)