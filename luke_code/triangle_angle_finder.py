a = float(input('angle a: '))
b = float(input('angle b: '))
if a+b < 180:
    c = 180 - (a+b)
    print (f"angle c is {c} degress")
if a+b >= 180:
    print("too big over 180 degress")

