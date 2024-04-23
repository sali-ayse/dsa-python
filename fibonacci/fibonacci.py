# Source of description: https://www.w3schools.com/dsa/dsa_algo_simple.php

# Fibonacci algorithm:
#
#
# 1. Start with the two first Fibonacci numbers 0 and 1.
#  a. Add the two previous numbers together to create a new Fibonacci number.
#  b. Update the value of the two previous numbers.
# 2. Do point a and b above 18 times.
#
# Source above


# 1. Fibonacci implementation with a for loop
def fibonacci_for_loop():
    first = 0
    second = 1
    for i in range(17):
        newVal = first + second
        print("Val:", newVal)
        first = second
        second = newVal


# 2. Fibonacci implementation with recursion
counter = 2


def fibonacci_recursion(first, second):
    global counter

    if counter <= 18:
        newVal = first + second
        print("Val, rec:", newVal)
        first = second
        second = newVal
        counter += 1
        fibonacci_recursion(first, second)
    else:
        return


# 3. Fibonacci implementation with recursion, finding the n-th Fibonacci number
counter = 2


def fibonacci_recursion_2(first, second, n):
    global counter

    if counter <= n:
        newVal = first + second
        print("n-th:", newVal)
        first = second
        second = newVal
        counter += 1
        fibonacci_recursion_2(first, second, n)
    else:
        return


# Code source: https://www.w3schools.com/dsa/dsa_algo_simple.php
def optimized_fibonacci(n: int):
    if n <= 1:
        return n
    else:
        return optimized_fibonacci(n-1) + optimized_fibonacci(n-2)


# Choose input
def choose_input():
    choice = int(input("Choose n: "))
    return choice


# Menu to select
def menu_function():
    while (True):
        print(
            "------------------------------------------------------------------------------")
        print("                                MENU")
        print(
            "------------------------------------------------------------------------------")
        print("1. Fibonacci implementation with a for loop")
        print("2. Fibonacci implementation with recursion")
        print(
            "3. Fibonacci implementation with recursion, finding the n-th Fibonacci number")
        print("4. Bonus round, optimized version for finding the n-th Fibonacci sequence")
        print("5. Exit the program")
        print(
            "------------------------------------------------------------------------------")

        global counter
        counter = 2

        answer = input()
        if answer == '1':
            fibonacci_for_loop()
        elif answer == '2':
            fibonacci_recursion(0, 1)
        elif answer == '3':
            fibonacci_recursion_2(0, 1, choose_input())
        elif answer == '4':
            print(optimized_fibonacci(choose_input()))
        elif answer == '5':
            print("Bye, have a nice day!")
            break
        else:
            print("Wrong input.")


menu_function()
