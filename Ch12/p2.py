# Write a program to print third, fifth and seventh element from a list using enumerate function.

l = [1,2,3,4,5,6,7,8]

for i,item in enumerate(l):
    if(i%2==0 and i!=0):
        print(i,item)
