t = [3, 8.5, 9, 9.5]
u = 3, 8.5, 9, 9.5
print(t)
print(u)

t[0] = 35
print(t)

#convert a list to a tuple this is also called casting
v = tuple(t)            #tuple converted from a list
print(v)
w = list(u)             #list converted from a tuple

#tuple slicing
print(u[1:3])

print("lowest number: ", min(u))
print("highest number: ", max(u))