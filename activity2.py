i=input("Enter a word:")
n=input("Enter a letter of that word:")
x=0
count=0
while(x<len(i)):
    if (i[x]==n):
        count+=1

    x+=1
print("The number of ",n,"is",count)

