def greet(name):
    print(f"Hello, {name}!")

name = input("Enter your name: ")
greet(name)

fruits = ["Apple", "Banana", "Cherry"]
for f in fruits:
    print(f"- {f}")

new = input("Add a fruit: ")
fruits.append(new)
print("Updated list:", fruits)
