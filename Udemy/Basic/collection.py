list1 = [10,20,30,40,50,50]
list1.insert(0, 100)
print(list1)
print(type(list1))

tuple1 = (10,20,30,40,50,50)
print(tuple1)
print(type(tuple1))

set1 = {10,20,30,40,50,50}
print(set1)
print(type(set1))
print("\n")

dict1 = {
    'roll':101,
    'name':"aaditya",
    'city':"Antri Deshmukh"
}
print(dict1)
for k,v in dict1.items():
    print(k, v)
