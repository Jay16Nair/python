# Exception Handling

try:
    num=int(input("Enter a number to divide "))
    den=int(input("Enter a number to divide by "))
    res=num/den
except ZeroDivisionError as e:
    print(e)
    print("Can't divide by zero")
except ValueError as e:
    print(e)
    print("Enter numbers only")
except Exception as e:
    print(e)
    print("Something wrong!")
else:
    print(res)
finally:
    print("This will always execute")