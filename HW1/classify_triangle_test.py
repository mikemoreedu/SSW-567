"""#performs various tests on classify_triangle.py"""
from classify_triangle import classify_triangle

def test_classify_triangle(): """testing various cases on classify_triangle()"""

assert classify_triangle(3, 4, 5) == "Scalene Right"
assert classify_triangle(5, 5, 5) == "Equilateral"
assert classify_triangle(5, 5, 7) == "Isosceles"
assert classify_triangle(3, 3, 4) == "Isosceles"
assert classify_triangle(2, 3, 4) == "Scalene"
assert classify_triangle(5, 7, 9) == "Scalene"
assert classify_triangle(8, 15, 17) == "Scalene Right"
assert classify_triangle(0, 0, 0,) == "Not a Triangle"
assert classify_triangle(1, 2, 5,) == "Not a Triangle"
