

##using split function to split user input according to space
#using map to convert each string to integer after splitting
numbers= list(map(int, input("Enter list of integers: ").split()))
#generate lists
zeros=[]
x=[]

#create a function that takes from user and define integers 
# if zero append to zeros list if not append to x list 
def  move_zeros(numbers):
    for i in range (len(numbers)):
        if numbers[i] != 0:
            x.append(numbers[i])
        else:
            zeros.append(numbers[i])
    return x+zeros


result = move_zeros(numbers)
print(result)



