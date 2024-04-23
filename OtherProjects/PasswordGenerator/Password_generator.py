import random
import string 

def generate_random_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letters 
    
    if numbers:
        characters += digits
    elif special_characters:
        characters += special
        
    password = ""
    meets_condition = False
    is_number = False
    is_special = False
        
    while not meets_condition or len(password) < min_length:
        new_chars = random.choice(characters)
        password += new_chars
        
        if new_chars in digits:
            is_number = True
        elif new_chars in special:
            is_special = True
            
        meets_condition = True
        
        if numbers:
            meets_condition = is_number
        elif special_characters:
            meets_condition = meets_condition and is_special
            
    return password 

min_length = int(input("Enter the password minimum length: "))
password = generate_random_password()
print(password)