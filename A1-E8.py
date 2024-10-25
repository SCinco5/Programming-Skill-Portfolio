"""Exercise 8: Simple Search"""


# the list of names to search 
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# ask the user to input the search term
search_term = input("Enter the name you are looking for: ")


lowercase_names = [name.lower() for name in names]
search_term_lower = search_term.lower()

# search for the term in the list
if search_term_lower in lowercase_names:
    print(f"{search_term} found in the list!")
else:
    print(f"{search_term} not found in the list.")
