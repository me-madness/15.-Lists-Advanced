# First way from the Lector

def sort_names():
    names_list = [name for name in input().split(', ')]
    
    return sorted(names_list, key=lambda x: (-len(x), x))

print(sort_names())

# Second way from me and lector 

names = input().split(', ')
sorted_names = sorted(names, key=len, reverse=True)
print(sorted(sorted_names, key=lambda x: (-len(x), x)))

# Third way from me 