"""Exercise 10: Is it even?"""

# def function then determine using the function to see if a number is even or odd
def check_even_or_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

# main function
def main():
    # ask the user for a number
    number = int(input("Enter a number: "))

    # call the function to check if the number is even or odd
    result = check_even_or_odd(number)

    # print the result
    print(result)

# call the main function when the script is executed
if __name__ == "__main__":
    main()
