#Taking input from user until he guesses the correct number by hinting him accordingly
#no. of guesses 9
#print no of guesses left
#print no of guesses he took to finish
#game over

n = 19
count = 0
num_of_guesses = 1
print("Number of guesses is limited to only 9 times")
while(num_of_guesses<=9):
    count = count + 1
    guess = input("Guess the number: ")
    guess = int(guess)
    if(guess==n):
        print("Congrats you've guessed the number correctly")
        print("Number of guesses you took to finish is "+str(count))
        break
    elif(guess<n):
        print("The number guessed is smaller...")
        print("Try again")
    elif(guess>n):
        print("The number guessed is greater...")
        print("Try again")
    print("Number of guesses left is "+str(9 - num_of_guesses))
    num_of_guesses = num_of_guesses + 1
if(num_of_guesses>9):
    print("Game Over!")

"""
OUTPUT:-
Enter a number: 12
The number guessed is smaller...
Try again
Number of guesses left is 8
Enter a number: 15
The number guessed is smaller...
Try again
Number of guesses left is 7
Enter a number: 20
The number guessed is greater...
Try again
Number of guesses left is 6
Enter a number: 18
The number guessed is smaller...
Try again
Number of guesses left is 5
Enter a number: 19
Congrats you've guessed the number correctly
Number of guesses you took to finish is 5

Process finished with exit code 0
"""