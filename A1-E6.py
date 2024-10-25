"""Exercise 6: Brute Force Attack"""


# define the correct password first
correct_password = "12345"

# max number of attempts the user gets
max_attempts = 5
attempts = 0

# while loop to keep asking until the correct password is entered or if their attempts run out
while attempts < max_attempts:
# ask the user to input the password
    entered_password = input("Enter the password: ")

    # then check if the entered password is correct
    if entered_password == correct_password:
        print("Password correct. Entering.")
        break
    else:
        # increment the number of attempts
        attempts += 1
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"Wrong password. You have {remaining_attempts} attempt(s) left.")
        else:
            print("Too many failed attempts. The cops are coming.")
