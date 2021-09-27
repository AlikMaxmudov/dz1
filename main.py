import math

def p(sides1, sides2, sides3):
return 1/2 * (sides1+sides2+sides3)

def s(sides1, sides2, sides3):
return math.sqrt(p(sides1, sides2, sides3) * (p(sides1, sides2, sides3)-sides1) * (p(sides1, sides2, sides3)-sides2) * (p(sides1, sides2, sides3)-sides3))

def trch(sides1,sides2,sides3):
return bool((sides1 + sides2 > sides3) and (sides2 + sides3 > sides1) and (sides3 + sides1 > sides2))

storony = input('Enter sides splited with space: ')
sides = storony.split(' ')
for i, item in enumerate(sides):
sides[i] = int(item)
sides.sort()
print(sides)
m = 0
for i in range(len(sides)):
if sides[i] <= 0:
print('index out of range!')
exit()
for i in range(1, len(sides)-1):
n = s(sides[i-1], sides[i], sides[i+1])
if n > m:
m = n
s1 = sides[i - 1]
s2 = sides[i]
s3 = sides[i + 1]

print('a =',s1, 'b =', s2, 'c =', s3)
print('A perimetr of the triangle is :', 2 * p(s1, s2, s3))
print('An area of the triangle is :',m)