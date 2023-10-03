print("Hello from VS code")
fname="Jayanth" 
lname="Nair"
print("Hello "+fname+ " " +lname)
age=19
print(type(age))
print("My age is "+str(age))
print(type(age))
height=250.5
print(type(height))

# multiple assignment
name , rollno , cgpa = "Jayanth",2211003011303,9.93
print(name)
print(rollno) 
print(cgpa)

Jay=Ris=Aman=105
print(Jay)
print(Ris)
print(Aman)

# string methods
print(len(name))
print(name.find("J"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name*3)

# slice[start:stop:step]
print(name[0:3])
print(name[3:])
print(name[0:8:2])
print("Reversed Name")
print(name[::-1])
website="https://www.google.com/"
slice=slice(12,-5)
print(website[slice])