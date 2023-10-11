# First way from the Lector

   

# Second way from me 

def even_numbers():
    numbers = input().split(', ')
    
    even_number = list(filter(lambda x: x % 2 == 0), numbers)
    return even_number

print(even_numbers())  