# update touple in case of some error

thisIsTuple = ("red", "green", "blue", "voilet", "indigo", "yellow")
print(thisIsTuple)

l = list(thisIsTuple)
l[0] = "purple"
print(l)
l.append("red")

t = tuple(l)
print(t)

i = 1
for a in t:
    print(i," ",a)
    i += 1