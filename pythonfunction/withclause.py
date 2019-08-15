with open("C:/Users/tin2419/Desktop/language.txt",'r') as file1:
    print(file1.read())

#HERE WITH THE 'WITH' CLAUSE THE FILE WILL BE AUTOMATICALLY CLOSED (IT GIVES TRUE AS A RESPONSE TO print(file1.closed)
print(file1.closed)
# THE ABOVE STATEMENT WILL GIVE TRUE WHEN WE USE THE WITH COMMAND T