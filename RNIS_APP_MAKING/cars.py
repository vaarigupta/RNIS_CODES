cars = ["Honda", "maruti" , "hyundai"]
car_1 = ["CADILLAC","lambo"]
num = [1,3,5,6,7,9]
print(cars)
#append - works in the end of the list 
#pop
#remove
#insert
#extend
#sort
#reverse
#in
#len
#type
cars.remove("Honda")
print(cars)
cars.pop()
print(cars)
cars.insert(1,"BMW")
print(cars)
cars.append("FERRARI")
print(cars)
cars.extend(car_1)
print(cars)
print(cars.index("FERRARI"))
num.sort()
print(num)
num.reverse()
print(num)
print(num[0:3:2])
for i in range(0,12,3):
    print(i)
    
for i in range(len(cars)):
    print(cars[i])

dict1 = { 'key1' :'value','key2':1,'key3':[1,2,3]}
print(dict1)
print(dict1['key3'])

dict2 = {'k1': 1,'k2' :'hello' ,'k3':2.7}
dict2['k5']='new key'
print(dict2)
del dict2['k3']
print(dict2)

##for key in dict1:
##    print(dict1[key])

print(type(dict1))
print(dict1['key3'][2])















