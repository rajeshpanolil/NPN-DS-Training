file1=open("C:/Users/tin2419/Desktop/language.txt",'r')
#TO READ A COMPLETE LINE AS A STRING
print(file1.read())

#to read line by line
#for line in file1:
    print(line)
   print("Reading line")

print(file1.readlines())
#IN THIS CASE, IT READS THE ENTIRE LINE AS A LIST

#CREATE A FILE AND TELL ME HOW MANY WORDS THAT FILE CONTAINS

content = file1.read()
print(type(content))
print("The number of words are", len(content.split(" ")))
#file1.seek(0,0) - to read a file multiple times to go back to the starting position of read


#TO WRITE A FILE
file2=open("C:/Users/tin2419/Desktop/language_new.txt",'w')
content = file2.read()
file2.write(content)
print(file2.close())
file2.close()
# IN BOTH CASES THE FILES REMAIN OPEN. LIKE FILE1.CLOSED WILL GIVE FALSE. SO WE HAVE TO EXPLICITLY CLOSE THE FILE