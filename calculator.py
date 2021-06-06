# Calculator Applicationusing Python Programming
#Author: Goura Koti
#Date: 06/06/2021

#Usage of array concept:
#The n number of operands are taken as input and stored in an array
import array as myarray

#Usage of functions and for loop
def getTerms(terms, elements):
    index=0
    for i in range(terms):
        value = int(input())
        elements.insert(index,value)
        index+=1
    
#reading an integer value
print ("How many operands do you have?")
terms = int(input())

#creating an empty integer array
elements = myarray.array('i',[])
print ("Enter", terms, "operands")
getTerms(terms, elements)

print("Enter your choice")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")

choice = int(input())
#Usage of if-else concept
if choice == 1:
    result = 0
    for i in range(terms):
        result += elements[i]
    print("Sum of operands is", result)
elif choice == 2:
    result = elements[0]
    for i in range(1,terms):
        result -= elements[i]
    print("Difference of operands is", result)
elif choice == 3:
    result = elements[0]
    for i in range(1,terms):
        result *= elements[i]
    print("Product of operands is", result)
elif choice == 4:
    result = elements[0]
    for i in range(1,terms):
        result /= elements[i]
    print("Quotient of operands is", result)
else:
    print ("You have made invalid choice !!")

print("Good Day:)")
