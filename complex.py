r1 = int(input("Enter the real part of the first complex number: "))
i1 = int(input("Enter the complex part of the first complex number: "))
r2 = int(input("Enter the real part of the second complex number: "))
i2 = int(input("Enter the complex part of the second complex number: "))

r = r1 + r2
i = i1 + i2

print("The addition of complex numbers is", r, "+", i, "i")

r11 = r1 - r2
i11 = i1 - i2

print("The subtraction of complex numbers is", r11, "-", i11, "i")

r22 = r1 * r2
i22 = i1 * i2

print("The multiplication of complex numbers is", r22, "+", i22, "i")

r33 = r1 / r2
i33 = i1 / i2

print("The divisionion of complex numbers is",r33 ,"+", i33, "i")