"""
takes args a, b, c and classifies them as a type of triangle, or not a triangle"""
side_length_a = int(input("Enter side length a: "))
side_length_b = int(input("Enter side length b: "))
side_length_c = int(input("Enter side length c: "))

def classify_triangle(side_a,side_b,side_c):
    """check if triangle is valid first, then check for each type of triangle and right triangles"""
    right_1 = side_a**2 + side_b**2
    right_2 = side_a**2 + side_c**2
    right_3 = side_b**2 + side_c**2
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return "Not a Triangle"
    if side_a + side_b < side_c or side_a + side_c < side_b or side_b + side_c < side_a:
        return "Not a Triangle"
    if side_a == side_b and side_b == side_c:
        return "Equilateral"
    if side_a == side_b or side_a == side_c or side_b == side_c:
        return "Isosceles"
    if right_1 == side_c**2 or right_2 == side_b**2 or right_3 == side_a**2:
        return "Scalene Right"
    return "Scalene"
#also comment the following two lines when testing
classify_triangle(side_length_a,side_length_b,side_length_c)
print(classify_triangle(side_length_a,side_length_b,side_length_c))
