#print("First Module is",__name__)

#To define a function

def sum(a,b):
    return a+b

if __name__== '__main__':
    print(sum(10,20))
else:
    print("YOu are calling from a second module")

#HERE THE __name__=='__main__' will execute if the function sum is called from the same module. If it is called
#from another module (imported), then the else clause will be executed

