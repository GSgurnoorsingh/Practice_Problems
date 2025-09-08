name=input("Enter your name:")
age=int(input("Enter your age:"))
current_year=2025
while (age<=100):
    current_year=current_year+1
    age+=1
    
print(f'{name} will be 100 years old in the year {current_year}')