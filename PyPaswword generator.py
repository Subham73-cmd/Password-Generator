import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to Python Password Generator")
no_of_letter=int(input("Enter the number of letters in password. \n")) #Enter the no of letters
no_of_numbers=int(input("Enter the numbers in password. \n"))  #Enter the no of numbers
no_of_symbols=int(input("Enter the number of symbols in password. \n")) #Enter the no of symbols
password_list=[]
for i in range(0,no_of_letter):
    password_list.append(random.choice(letters))
for i in range(0,no_of_numbers):
    password_list.append(random.choice(numbers))
for i in range(0,no_of_symbols):
    password_list.append(random.choice(symbols))
#print(password_list)-->Prints the password list
random.shuffle(password_list) #Shuffles the password list
#print(password_list)-->Prints the shuffles password list
password=""
for i in password_list:
    password+=i
print(f"Your password is {password}")