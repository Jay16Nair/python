#list in python
names=["Jayanth","Rishaan","Aman","Dhruv","Aditya"]
print(names)
print(names[0])
print(names[0:2])
print(names[::-1])

names[4]="AVS"

names.append("Naman")

for i in names:
    print(i)

names.remove("Dhruv")
print(names)
names.insert(3,"Dhruv")
names.sort()
print(names)

# 2D lists

drinks=["coffee","tea","coke"]
dinner=["pizza","burger","pasta"]
dessert=["cake","ice cream"]

food=[drinks,dinner,dessert]
print(food)
print(food[0])
print(food[2][1])