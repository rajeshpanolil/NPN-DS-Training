def sum_num(a, b):
    return a+b,a-b


a,b = sum_num(12, 10)
print(a,b)
print(sum_num(b=20,a=30))
#The above statement gives default values to the sum_num function

def sum_num(a, b=10):
    return a+b,a-b

a,b = sum_num(12, 10)
print(a,b)
print(sum_num(b=20,a=30))
# In this case, b - 20 will be taken and not the default value of 10 for b
# your default value should be at the end and not at the beginning
#Create a function which will take a list as input but the return will be two lists - odd and even

def split_list(list1):
    list2, list3 = [],[]
    for i in list1:
        if i%2 == 0:
            list2.append(i)
        else:
            list3.append(i)
    return list2, list3


list1 = [1,2,3,4,5,6,7,8]
even,odd = split_list([list1])
print(even,odd)

#VARIABLE ARGUMENT IN FUNCTIONS

def multiplication(*args):
    mul = 1
    for i in args:
        mul = mul*i
        return mul

print(multiplication(1,2,3,4,5))

# TO CONCATENATE WHATEVER ARGUMENT WE GET AND THEN PRINT IT

def concatenator(*args):
    first = ''
    for i in args:
        first = first + i + " "
    return first
#Here *args ensures that we have no restriction put on the inputs

print(concatenator("Have","a","nice","day"))

#KEY WORD VARIABLE LENGTH ARGUMENT (**KWARGS) ALSO, ALWAYS VARIABLE LENGTH WILL BE AFTER THE FIXED VARIABLES (a,b,*args)

def print_kwargs(**kwargs):
    for key,val in kwargs.items():
        print(key,val)

print_kwargs(Id =1, name= 'Ramesh')

# TO PRINT EMPID, NAME, WE NEED TO USE ZIP SO THAT WE CAN GET THE VALUES SIDE BY SIDE. ALSO REMEMBER TO USE LIST OTHERWISE ZIP WILL ONLY RETURN OBJECT


