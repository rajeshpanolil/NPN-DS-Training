#THREE MORE IMPORTANT FUNCTIONS - MAP, FILTER AND REDUCE AND BEFORE THAT LAMBDA EXPRESSION

# TO SQUARE TWO NUMBERS: Lambda is a quicker way to do the mathematical calculations - simple ones
# TRADITIONAL WAY
def square(a):
    return a**2

lambda x:x**2
lambda x,y: x+y

#Lambda is an anonymous function - no name. Can write simple functions easily. It can be stored in some variable and call it

calculate = lambda x,y:x+y
print(calculate(10,20))

#MAP FUNCITON. map(func,list)
def square(x):
    return x**2

list1 = [10,20,30,40]

print(list(map(square,list1)))
# this can be done in another way - what is normally written

print(list(map(lambda x:x**2,list1)))

#TO GO THROUGH A LIST AND THEN FIND THE LENGTH OF EACH STRING USING LAMBDA
list2 = ["ABC","CD"]
print(list(map(lambda x:len(x),list2)))

#FILTER FUNCTION - filter(function,list) - will filter the list based on the function specified and is run on each -
# - element. Map gives all the records but filter will only give those items that match the conditions
list1 = [10,20,30,40,43,53]
print(list(filter(lambda x: x%2==0,list1)))

#REDUCE IS NOT VERY FREQUENTLY USED - UNLIKE MAP, FILTER AND LAMBDA - REDUCE EXECUTES SUCCESSIVE ITEMS -
# - LIKE TWO AT A TIME OR CUMULATIVE

#reduce (lambda x,y:y-x,list1) [10,20,30] LIKE IT WILL WORK ON 10 AND 20, THE RESULT OF THAT - 10 WILL BE USED -
# - TO WORK ON 30 ETC - LIKE FIBONAICI SEQUENCE




