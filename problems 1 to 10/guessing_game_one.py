import random

keep_playing = True

while keep_playing:
    n = random.randint(1, 9)  
    guess_count = 0
    
    while True: 
        number = int(input("Enter your guess between 1 to 9: "))
        guess_count += 1
        
        if n == number:
            print("Correct guess!")
            print(f"You guessed correctly in {guess_count} attempts.")
            
            play_again = input("Do you want to play again (y/n)? ")
            if play_again == 'y':
                keep_playing = True  
                break 
            else:
                keep_playing = False 
                break  
            
        elif n in range(1, 6):
            if number in range(1, 6):
                print("You are very close!")
            else:
                print("Very far from the correct guess")
        elif n in range(6, 10):
            if number in range(6, 10):
                print("You are very close!")
            else:
                print("Very far from the correct guess")
