import random

game_on=True

print("Welcome to rock paper scissors game!")
name=input("Please enter your name to continue:")

while game_on:
    ch=input("Enter your choice(r,p,s):")
    comparison_dict={'r':0,'p':1,'s':2}
    comp_choice=random.choice([0,1,2])
    comp_comparison_dict={0:'Rock',1:'Paper',2:'Scissors'}
    choice=comparison_dict[ch]
    
    print(f"You chose {comp_comparison_dict[choice]} and computer chose {comp_comparison_dict[comp_choice]}")
    
    if (comp_choice==choice):
        print("It's a draw")
    else:
        if(comp_choice==1 and choice==0):
            print("Computer Wins!")
        elif(comp_choice==1 and choice==2):
            print(f"{name} Wins!!")
        elif(comp_choice==0 and choice==1):
            print(f"{name} Wins!!")
        elif(comp_choice==0 and choice==2):
            print("Computer Wins!")
        elif(comp_choice==2 and choice==1):
            print("Computer Wins!")
        else:
            print(f"{name} Wins!!")
    
    again=input("Do you want to play again(y/n)?".lower())
    if (again=='y'):
        game_on
    else:
        print("Bye bye hope to play with you again!")
        game_on=False