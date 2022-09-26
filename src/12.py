from math import sqrt
a = int(input())
b = int(input())
c = int(input())

p = (a + b + c) / 2
s = sqrt(p * (p-a) * (p-b) * (p-c))

h1 = 2 * s / a
h2 = 2 * s / b
h3 = 2 * s / c

m1 = sqrt(2 * a**2 + 2 * c**2 - b**2) / 2
m2 = sqrt(2 * b**2 + 2 * c**2 - a**2) / 2
m3 = sqrt(2 * a**2 + 2 * b**2 - c**2) / 2

la = sqrt(b * c * (a+b+c) * (b+c-a)) / (b+c)
lb = sqrt(a * c * (a+b+c) * (a+c-b)) / (a+c)
lc = sqrt(a * b * (a+b+c) * (a+b-c)) / (a+b)

r = (((p-a)*(p-b)*(p-c))/p)**0.5
R = (a*b*c)/(4*((p*(p-a)*(p-b)*(p-c))**0.5))