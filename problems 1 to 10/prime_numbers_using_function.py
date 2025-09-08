def is_prime(n):
    if (n<=1):
        flag=False
    elif(n==2):
        flag=True
    else:
        flag=True
        for i in range(2,n):
            if n%i==0:
                flag= False
                break
            
    if flag:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")
                
n=int(input("Enter the number:"))
is_prime(n)