
a, b, c = 1., 2., 1 # => a et b seront du type 'float'
while c <18:
    a, b, c = b, b*a, c+1
    print(b)