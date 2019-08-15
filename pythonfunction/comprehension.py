list1 = range(10)
odd = []
even = []
for i in list1:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

#using comprehension we can do the above code in one line

even = [i for i in list1 if i%2 ==0]
# even = [output list for <var> in list1 <condition> ]
odd = [i for i in list1 if i%2 != 0]
print(odd)

# COMPREHENSION WILL WORK ONLY IF IT HAS AN IF CONDITION

# DICTIONARY COMPREHENSION - THE OUTPUT IS A DICTIONARY - EFFICIENT WAY TO CREATE A DICTIONARY FROM AN EXPRESSION
list1 = [1,2,3,4]
dict1 = {i:1**2 for i in list1}
print(dict1)

list1 = ["id","name"]
list2 = [1,"Ramesh"]
dict2 = {key:val for key,val in zip(list1,list2)}
print(dict2)



