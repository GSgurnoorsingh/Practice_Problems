stri=input("Enter a string:")
for i in stri:
    if i[0:]==i[::-1]:
        print(f"{stri} is a palindrome")
        break
    else:
        print(f"{stri} is not a palindrome")
        break