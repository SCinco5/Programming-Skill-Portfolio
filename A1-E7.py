"""Exercise 7: Some Counting""" 


# loop that counts up from 0 to 50 in increments of 1 
print("Counting up from 0 to 50:")
for a in range(0, 51):  # range(start 0, stop 51) 
    print(a)

# loop that counts down from 50 to 0 in decrements of 1 
print("\nCounting down from 50 to 0:")
for a in range(50, -1, -1):  # range(start 50, stop -1, step -1) 
    print(a)

# loop that counts up from 30 to 50 in increments of 1 
print("\nCounting up from 30 to 50:")
for a in range(30, 51):  # range(start 30, stop 51) 
    print(a)

# loop that counts down from 50 to 10 in decrements of 2 
print("\nCounting down from 50 to 10 in decrements of 2:")
for a in range(50, 9, -2):  # range(start 50, stop 9, step -2) 
    print(a)

# loop that counts up from 100 to 200 in increments of 5 
print("\nCounting up from 100 to 200 in increments of 5:")
for a in range(100, 201, 5):  # range(start 100, stop 201, step 5) 
    print(a)
