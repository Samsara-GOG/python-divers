a, b, c = 1., 2., 1
while c < 18:
    a, b, c = b, b*a, c+1
    print(c, ":", b)