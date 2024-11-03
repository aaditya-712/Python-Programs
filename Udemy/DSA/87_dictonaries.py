# Dictonary
# key : value

customer = {
    "name" : "Aaditya",
    "email" : "aadi712@gmail.com",
    "phone" : 758808,
    "verified" : True
}

print(customer)
print(customer["name"])

# update existing data
customer["name"] = "Nikhil"
print(customer)

# add new key value
customer["pincode"] = 443301
print(customer)

# remove any key use 'pop()'
customer.pop("phone")
print(customer)