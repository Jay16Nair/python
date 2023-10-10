# set of key value pairs

captains={'MI':'Rohit','CSK':'Mahi','RCB':'Virat','LSG':'KL Rahul'}
print(captains['MI'])
print(captains.keys())
print(captains.values())

for key,value in captains.items():
    print(key, value)

captains.update({'GT':'Hardik'})
print(captains)