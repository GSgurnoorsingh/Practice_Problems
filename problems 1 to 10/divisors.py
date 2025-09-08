n=int(input("Enter a no between 1 to 100:"))
x=[i for i in range(1,101)] 
y=[]
for j in x:
    if(n%j==0):
        y.append(j)
z=','.join(map(str,y))
print(f"The divisors of {n} are : {z}")