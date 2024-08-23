# join lists

names = ["Aaditya", "Kartik", "Nikhil", "Ram", "Ankush"]
countries = ["India", "USA", "Russia", "Japan", "Germany"]

# 1
# result = names + countries
# print(result)


# 2
# for i in names:
#     countries.append(i)
# print(countries)


# 3
names.extend(countries)
print(names)