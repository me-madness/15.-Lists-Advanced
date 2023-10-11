# First way from the Lector

def even_numbers():
    numbers = input()
    
    even_number = list(filter(lambda x: x % 2 == 0), numbers)
    return even_number

print(even_numbers())    

# Second way from me 
