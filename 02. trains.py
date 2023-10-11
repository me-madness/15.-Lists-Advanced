# First way from the Lector

wagons = [0] * int(input())

while True:
    command = input().split()
    
    if command == 'End':
        print(wagons)
        break
    
    elif command == 'add':
        number_of_people = int(command[1])
        wagons[-1] += number_of_people
        
    elif command[0] == 'insert':
        index = int(command[1])    
        people = int(command[2])    
        
    elif command[0] == 'leave':
        index = int(command[1])    
        people = int(command[2]) 
            
         
            
# Second way from me            