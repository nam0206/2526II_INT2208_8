import unittest
from Triangle import triangle
class TestTriangle(unittest.TestCase):


    def test_invalid_input_less_or_equal_zero(self):
        self.assertEqual(triangle(0, 5, 5), "Invalid Input ")
        self.assertEqual(triangle(0,0,0), "Invalid Input ")

    def test_invalid_input_greater_than_1000(self):
        self.assertEqual(triangle(1001, 5, 5), "Invalid Input ")
        self.assertEqual(triangle(5, 1001, 5), "Invalid Input ")
        self.assertEqual(triangle(5, 5, 1001), "Invalid Input ")

   
    def test_not_a_triangle(self):
   
        self.assertEqual(triangle(1, 2, 3), "Not a Triangle")
        self.assertEqual(triangle(2, 2, 10), "Not a Triangle")

  
    def test_equilateral_triangle(self):
        self.assertEqual(triangle(5, 5, 5), "Equilateral")
        self.assertEqual(triangle(100, 100, 1000), "Equilateral")
        self.assertEqual(triangle(1, 1, 1), "Equilateral")

    def test_isosceles_triangle(self):
        self.assertEqual(triangle(5, 5, 3), "Isosceles") 
        self.assertEqual(triangle(5, 3, 5), "Isosceles") 
        self.assertEqual(triangle(3, 5, 5), "Isosceles") 

    def test_scalene_triangle(self):
        self.assertEqual(triangle(3, 4, 5), "Scalene")
        self.assertEqual(triangle(6, 8, 10), "Scalene")

if __name__ == '__main__':
    unittest.main()