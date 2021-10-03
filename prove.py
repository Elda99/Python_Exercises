""""
A program to calculate average marks
of n students where n is entered by
the user.
"""
n =int(input("Enter number of users: "))
i=0
list1=[]
while(i<n):
    marks= float(input("Enter marks: "))
    list1.append(marks)
    i=i+1
    sum=0
    for marks in list1:
        sum=sum+marks
        avg=sum/n

print(avg)
