import time
for i in range(0,11,2):
    print(i)
for i in "Jayanth":
    print(i)
for i in range(10,0,-1):
    print(i)
    time.sleep(1)

rows=int(input("Enter number of rows "))
cols=int(input("Enter number of cols "))

for i in range(rows):
    for j in range(cols):
        print("*",end="")
    print()

ph_num="123-456-789"
for i in  ph_num:
    if i == "-":
        continue
    print(i,end="")

for i in range(0,5):
    if i == 3:
        pass
    else:
        print(i)