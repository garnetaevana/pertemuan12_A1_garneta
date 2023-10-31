# import module matematika math
import math
# Input koefisien dari keyboard
a = int(input('Masukkan a: '))
b = int(input('Masukkan b: '))
c = int(input('Masukkan c: '))
# hitung diskriminan d
d = (b**2) - (4*a*c)
# cek nilai diskriminan
# menemukan x1 dan x2
if d >= 0 :
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d))/(2*a)
    print("Solusinya adalah {0} dan {1}".format(x1, x2))
else: # akar kompleks 
    real = b / (2*a)
    imajiner = math.sqrt(abs(d)) / (2*a)
    print("Solusinya adalah {0} + {1}i dan {0}-{1}i".format(real, imajiner))



import cmath
# Input coefficients
a = int(input('Masukkan a: '))
b = int(input('Masukkan b: '))
c = int(input('Masukkan c: '))

# Calculate discriminant
d = (b**2) - (4*a*c)

# Calculate roots
x1 = (-b+cmath.sqrt(d))/(2*a)
x2 = (-b-cmath.sqrt(d))/(2*a)

print("Solusinya adalah {0} dan {1}".format(x1, x2))