"""#performs various tests on classify_triangle.py"""
from classify_triangle import classify_triangle

def test_classify_triangle(): """testing various cases on classify_triangle()"""

assert classify_triangle(0, 0, 0) == "Not a Triangle"
assert classify_triangle(1, 1, 1) == "Equilateral"
assert classify_triangle(2, 2, 3) == "Isosceles"
assert classify_triangle(3, 3, 3) == "Equilateral"
assert classify_triangle(3, 4, 5) == "Scalene Right"
assert classify_triangle(4, 5, 6) == "Scalene"
assert classify_triangle(1, 1, 5) == "Not a Triangle"
