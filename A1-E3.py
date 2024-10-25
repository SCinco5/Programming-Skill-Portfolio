

"""Exercise 3: Biography"""


name=input('Enter your first name: ') #first i started by making the user input their information
name_two=input('Enter your second name: ')
hometown= input('Enter your hometown: ')
age=input('Enter your age: ')


while not age.isdigit():  #by doing this, if the user answers it in string, it'll be invalid
    print('Please enter a valid number for age. ')
    age = input('Enter your age: ')
age = int(age) #this converts the age into an integer

full_name = f"{name} {name_two}" #this will make the variables together in one line, to make your name complete

user_info = { #with this it stores the users information in a dictionary
    'Name': full_name,
    'Hometown': hometown,
    'Age': age
}


print('\nUser Information:') #then I print the values in separate lines
print('Name:', user_info['Name'])
print('Hometown: ', user_info['Hometown'])
print('Age: ', user_info['Age'])
