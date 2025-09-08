import random
import string
import time

lst=['!','@','#','$','%','^','&','*','-','_','+','?','/','(',')','=','{','}','[',']',':',';','"',"'",'<','>',',','.']

letters=string.ascii_letters
list_of_letters=list(letters)

digits=string.digits
digits_list=list(digits)

def weak():
    print("Generating your password.....")
    print('Please wait')
    time.sleep(1)
    small_letters=list(string.ascii_lowercase)
    small_letters.extend(digits_list)
    num_items=random.randint(6,8)
    weak_password=''.join(random.choices(small_letters,k=num_items))
    print("Here is your weak password:-")
    time.sleep(0.5)
    return weak_password

def middle():
    print("Generating your password.....")
    print('Please wait')
    time.sleep(1)
    random_symbol=random.choices(lst,k=2)
    list_of_letters.extend(digits_list)
    list_of_letters.extend(random_symbol)
    letter_items=random.randint(8,10)
    medium_password=''.join(random.choices(list_of_letters,k=letter_items))
    print("Here is your medium password:-")
    time.sleep(0.5)
    return medium_password

def strong():
    print("Generating your password.....")
    print('Please wait')
    time.sleep(1)
    list_of_letters.extend(digits_list)
    list_of_letters.extend(lst)
    letter_all=random.randint(12,16)
    strong_password=''.join(random.choices(list_of_letters,k=letter_all))
    print("Here is your strong password:-")
    time.sleep(0.5)
    return strong_password

print("Welcome to password generator!!")
time.sleep(1)

while True:
   choice=input("Pls enter the strength for your password(weak,medium,strong):").lower()
   if(choice=='weak'):
       print(weak())
       break
   elif(choice=='medium'):
       print(middle())
       break
   elif(choice=='strong'):
       print(strong())
       break
   else:
       print("Invalid input. Please type 'weak', 'medium', or 'strong'.")
       time.sleep(1)