# basic input
name = input()
city = input()

print("My name is", name, "\nI am from", city)

# input with prompt
name = input("Enter your name: ")
city = input("Enter your city: ")

print("My name is", name, "\nI am from", city)

# scan float
amount = float(input("Enter the amount: "))
rate = float(input("Enter the rate: "))

print("amount: ", amount)
print("intrest: ", rate)

# print is a build in standart output sys.stdout
print(city, name, amount, rate, sep=",", end="!\n")