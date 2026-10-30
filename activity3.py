x=int(input("Enter a number:"))
y=int(input("Enter a higher number then that:"))
count=0
for i in range(x,y):
    if i>1:
        for n in range(2,i):
            if (i%n==0):
                break
        else:
            print(i)
