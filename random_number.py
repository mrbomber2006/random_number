"""
This code returns a random number between the two numbers that the user asks for
"""
import random


def generate(numb1, numb2):
    x = random.randint(numb1, numb2)
    return x


number1 = int(input("please insert the first number:  "))
number2 = int(input("please insert the second number:  "))

result = generate(number1, number2)

def clean_number(number):
    number_str = str(number)
    if len(number_str) <= 3:
        return number_str
    else:
        return clean_number(number_str[:-3]) + ',' + number_str[-3:]
cleaner_result = clean_number(result)
print(cleaner_result)

# To understand the digit of the number


def Digit_of_numbers(num1):

    ragham = len(str(num1)) - 1
    if ragham > 29:
        raise IndexError 
    names = ["one", "ten", "hundred", "thousand", "ten thousand",
             "hundred thousand", "million", "ten million", "hundred million", "billion",
             "ten billion", "hundred billion", "trillion", "ten trillion", "hundred trillion",
             "quadrillion", "ten quadrillion", "hundred quadrillion", "quintillion", "ten quintillion",
             "hundred quintillion", "sextillion", "ten sextillion", "hundred sextillion", "septillion",
             "ten septillion", "hundred septillion", "octillion", "ten octillion", "hundred octillion"]
    return names[ragham] 


try:
    print(Digit_of_numbers(result))
except IndexError:
    print("Your number is too big! Bigger than a hundred octillion!")


print("done")
