#!/usr/bin/env python3
def admin_login(username, password):
    if username.toUpper() == "ADMIN" and password == "12345":
        return "Access granted"
    
    return "Access denied"

def how_theWeather(temperature):
    if temperature > 85:
        return "It's too dang hot out there!"
    
    elif 65 >= temperature >= 40:
        return "It's a little chilly out there!"
    
    elif temperature < 40:
        return "It's brisk out there!"
    
    return "It's perfect out there!"

def fizzbuss(number):
    if not number % 15:
        return "FizzBuzz"
    elif not number % 5:
        return "Buzz"
    elif not number % 3:
        return "Fizz"
    
    return number

def calculator(operation, numberOne, numberTwo):
    if operation == "+":
        return numberOne + numberTwo
    elif operation == "-":
        return  numberOne - numberTwo
    elif operation == "*":
        return  numberOne * numberTwo
    elif operation == "/":
        return  numberOne / numberTwo
    
    print("Invalid operation!")
    return "None"
