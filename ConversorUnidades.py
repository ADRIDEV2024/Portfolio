
def display_header():
    print()
    print("** UNIT CONVERTER **")
    print()

def display_conversions(conversions):
    print("Conversions available: \n")
    
    for conversion_number, from_unit, to_unit in conversions:
        print(f"{conversion_number}) {from_unit} -> {to_unit}")
    print()

def get_conversion_choice(conversions):
    
    conversion = input("Enter the number of conversion to use: ")
    conversion_index = int(conversion) - 1
    return conversions[conversion_index]

def get_conversion_value(from_unit):
    return float(input(f"Enter {from_unit} --> "))

def convert_value(conversion_number, from_value):
    conversion_functions = {
       
    }
    return conversion_functions[conversion_number](from_value)

def main():
    
    conversions = [
        (1, "km", "mi"),
        (2, "mi", "km"),
        (3, "kg", "lbs"),
        (4, "lbs", "kg"),
        (5, "ºF", "ºC"),
        (6, "ºC", "ºF"),
    ]
    
    display_header()
    display_conversions(conversions)
    
    conversion_number, from_unit, to_unit = get_conversion_choice(conversions)
    print()
    
    from_value = get_conversion_value(from_unit)
    print()
    
    to_value = convert_value(conversion_number, from_value)
    print(f"{from_value}{from_unit} --> {to_value}{to_unit}")

if __name__ == "__main__":
    main()
