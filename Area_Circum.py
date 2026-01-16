
def area_circum_circle(r):
    Area = 3.142*r*r
    Circumference = 2*3.142*r
    return (Area, Circumference)

r = 20
Area , Circumference = area_circum_circle(r)
print("Area of Circle:",Area)
print("Area of Circumference:",Circumference)
