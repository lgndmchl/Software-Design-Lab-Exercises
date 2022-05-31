from multiprocessing.sharedctypes import Value


number=int(input("Enter the grade:"))
if number>89:
    value ='1'
elif number >79:
    value ='2'
elif number>75:
    value ='3'
else:
    value= '4'

print("THE VALUE GRADE IS", value)