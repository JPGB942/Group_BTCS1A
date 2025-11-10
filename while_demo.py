# problem: Create a script where it will continously add a number

sum = 0
num = int(input("enter a number: (negative to quit) "))
while num >= 0:
    sum += num
    print(f"sum is {sum}")
    num = int(input("enter a number: (negative to quit) "))

print("negative number entered. program will stop")
