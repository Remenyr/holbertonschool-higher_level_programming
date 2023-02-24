import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_init(self):
        base1 = Base()
        self.assertEqual(base1.id, 1)

        base2 = Base(50)
        self.assertEqual(base2.id, 50)

    def test_from_json_string(self):
        json_string = '[{"id": 1}]'
        dictionary_list = Base.from_json_string(json_string)
        self.assertEqual(dictionary_list, [{"id": 1}])

    def test_to_json_string(self):
        base2 = Base(50)
        self.assertEqual(base2.to_json_string(None), "[]")
        self.assertEqual(base2.to_json_string([]), "[]")
        self.assertEqual(base2.to_json_string(base2.to_json_string([ {'id': 12} ])), '"[{\\"id\\": 12}]"')

if __name__ == '__main__':
    unittest.main()
