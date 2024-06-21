import random
import string 

def generate_random_password(min_length, numbers=True, special_characters):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letters 
    
    if numbers:
        characters += digits
    if special_characters:
        characters += special
        
    password = " "
    meets_condition = False
    is_number = False
    is_special = False
        
    while not meets_condition or len(password) < min_length:
        new_chars = random.choice(characters)
        password += new_chars
        
        if new_chars in digits:
            is_number = True
        if new_chars in special:
            is_special = True
            
        meets_condition = True
        
        if numbers:
            meets_condition = is_number
        if special_characters:
            meets_condition = meets_condition and is_special
            
    return password 

min_length = int(input("Enter the password minimum length: "))
is_number = input("Do you want numbers(yes/no)?: ").lower()
is_special = input("Do you want special characters(yes/no)?: ").lower()

password = generate_random_password(min_length, is_number, is_special)
print(password)
