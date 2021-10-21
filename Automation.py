import keyboard

#performing simple math problems that you already know how to do, but don't want to waste time doing it
a = int(input("Enter first number"))
b = int(input("Enter second number"))

def calc():
    if keyboard.read_key() == "a":
       sum = a + b
       print(sum)

    if keyboard.read_key() == "s":
        difference = a - b
        print(difference)

    if keyboard.read_key() == "m":
        product = a * b
        print(product)

    if keyboard.read_key() == "d":
        quotient = a / b
        print(quotient)
calc()