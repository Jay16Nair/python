marks=int(input("Enter your marks "))

if (marks > 80) :
    print("O grade")
elif ((marks > 60) and (marks <= 80)):
    print("A grade")
elif ((marks > 40) and (marks <= 60)):
    print("B grade")
else :
    print("Fail")

a = 7
b = 9
c = 3


if((a>b and a>c) and (a != b and a != c)):
	print(a, " is the largest")
elif((b>a and b>c) and (b != a and b != c)):
	print(b, " is the largest")
elif((c>a and c>b) and (c != a and c != b)):
	print(c, " is the largest")
else:
	print("entered numbers are equal")
