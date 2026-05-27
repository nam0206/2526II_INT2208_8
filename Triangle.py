def triangle(a,b,c):
    if a<=0 or b<=0 or c<=0 or a>100 or b>100 or c>100:
        return "Invalid Input "
    if a+b<=c or a+c<=b or b+c<=a:
        return "Not a Triangle"
    if a==b and b==c:
        return "Equilateral"
    if a==b or b==c or a==c:
        return "Isosceles"
    return "Scalene"
