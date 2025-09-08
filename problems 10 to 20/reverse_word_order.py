def reverse_true():
    s=input("Enter a string:")
    x=s.split()
    s=x[::-1]
    reversed_string=' '.join(s)
    return reversed_string

print(reverse_true())