import unittest
import os
from unittest.mock import patch, mock_open
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_init(self):
        square = Square(5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertIsNotNone(square.id)

    def test_size_property(self):
        square = Square(5)
        square.size = 10
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)


    def test_str(self):
        square = Square(5, 2, 3, 4)
        self.assertEqual(str(square), "[Square] (4) 2/3 - 5")

    def test_update(self):
        square = Square(5, 2, 3, 4)
        square.update(1, 10, 20, 30)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 20)
        self.assertEqual(square.y, 30)

        square.update(id=2, size=15, x=25, y=35)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 15)
        self.assertEqual(square.x, 25)
        self.assertEqual(square.y, 35)

    def test_to_dictionary(self):
        square = Square(5, 2, 3, 4)
        expected_dict = {"id": 4, "size": 5, "x": 2, "y": 3}
        self.assertDictEqual(square.to_dictionary(), expected_dict)

    def test_create_rectangle(self):
        rectangle_dict = {'id': 89}
        rectangle = Square.create(**rectangle_dict)
        self.assertEqual(rectangle.__str__(), "[Square] (89) 0/0 - 1")
        rectangle_dict = {'id': 89, 'size': 2 }
        rectangle = Square.create(**rectangle_dict)
        self.assertEqual(rectangle.__str__(), "[Square] (89) 0/0 - 2")
        rectangle_dict = {'id': 89, 'size': 2, 'x': 3}
        rectangle = Square.create(**rectangle_dict)
        self.assertEqual(rectangle.__str__(), "[Square] (89) 3/0 - 2")
        rectangle_dict = {'id': 89, 'size': 2, 'x': 3, 'y': 4}
        rectangle = Square.create(**rectangle_dict)
        self.assertEqual(rectangle.__str__(), "[Square] (89) 3/4 - 2")

    def test_save_to_file(self):
        list_squares = [Square(5, 2, 3, 4)]
        with patch('builtins.open', mock_open()) as mock_file:
            Square.save_to_file(list_squares)
            mock_file.assert_called_once_with('Square.json', mode='w', encoding='utf-8')
            mock_file().write.assert_called_once_with('[{"x": 2, "y": 3, "id": 4, "size": 5}]')

        list_squares = []
        with patch('builtins.open', mock_open()) as mock_file:
            Square.save_to_file(list_squares)
            mock_file.assert_called_once_with('Square.json', mode='w', encoding='utf-8')
            mock_file().write.assert_called_once_with("[]")
        
        list_squares = None
        with patch('builtins.open', mock_open()) as mock_file:
            Square.save_to_file(list_squares)
            mock_file.assert_called_once_with('Square.json', mode='w', encoding='utf-8')
            mock_file().write.assert_called_once_with("[]")

        list_squares = [Square(1, 2)]
        with patch('builtins.open', mock_open()) as mock_file:
            Square.save_to_file(list_squares)
            mock_file.assert_called_once_with('Square.json', mode='w', encoding='utf-8')
            mock_file().write.assert_called_once_with('[{"x": 2, "y": 0, "id": 32, "size": 1}]')

    def test_load_from_file(self):
        r1 = Square(10, 2, 8)
        r2 = Square(2, 4)
        list_rectangles_input = [r1, r2]

        # Save the list of rectangles to a file
        Square.save_to_file(list_rectangles_input)

        # Load the list of rectangles from the file
        list_rectangles_output = Square.load_from_file()

        # Check that the output list has the same length as the input list
        self.assertEqual(len(list_rectangles_input), len(list_rectangles_output))

        # Check that the rectangles in the output list have the same attributes as the rectangles in the input list
        for i in range(len(list_rectangles_input)):
            self.assertEqual(list_rectangles_input[i].to_dictionary(), list_rectangles_output[i].to_dictionary())

        # Delete the file
        os.remove("Square.json")

    def test_errors(self):
        with self.assertRaises(TypeError):
            square = Square("1")
        with self.assertRaises(TypeError):
            square = Square(1, "2")
        with self.assertRaises(TypeError):
            square = Square(1, 2, "4")

        with self.assertRaises(ValueError):
            square = Square(-1)
        with self.assertRaises(ValueError):
            square = Square(1, -2)
        with self.assertRaises(ValueError):
            square = Square(1, 2, -3)
        with self.assertRaises(ValueError):
            square = Square(0)

if __name__ == '__main__':
    unittest.main()
