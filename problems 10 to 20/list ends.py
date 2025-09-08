import random
def last_first_list_element(lst):
    l=[]
    for i in lst:
        l.append(lst[0])
        l.append(lst[-1])
        break
    print(l)

random_list=[random.randint(1,100) for _ in range(10)] #For getting a random list
print(random_list)
last_first_list_element(random_list)