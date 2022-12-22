a = int(input("Enter side length a: "))
b = int(input("Enter side length b: "))
c = int(input("Enter side length c: "))

def classify_triangle(a,b,c):
    if a <= 0 or b <= 0 or c <= 0 or a + b < c or a + c < b or b + c < a:
        return "Not a Triangle" 
    else:
        if a == b and b == c:
            return "Equilateral"
        elif a == b or a == c or b == c:
            return "Isosceles"
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "Scalene Right"
        else:
            return "Scalene"
#also comment the following two lines when testing
classify_triangle(a, b, c)
print(classify_triangle(a,b,c))
