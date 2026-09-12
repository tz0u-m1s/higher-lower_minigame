from random import randint
from time import sleep
times_played=0

while True:
    start_game=input("Start playing Higher/Lower? (Y/N)")

    if start_game=="Y" or start_game=="y":
        try:
         diff=int(input("Select Difficulty (1,2,3) "))
        except ValueError:
            print('oops, try again!')
        print("Starting game...")
        randnum=randint(1,100)
        sleep(1)
        print("Picking Number...")
        sleep(2)
        print("All done!")
        sleep(1)
        print("\n"*15)
        if diff==1:
           print("You have: 20 questions")
        if diff==2:
           print("You have: 15 questions")
        if diff=3:
           print("You have: 10 questions")
        question_amount=1
        question=int(input(f"Ask question no.{question_amount} Type 1 to see if it is higher or lower than a number you choose, 2 if you want to see an area of where the number is, and 3 if you want to see if the number is odd or even."))
        if question==1:
           higher_lower=input("Select a number to see if the secret number is higher or lower than it: ")
           if higher_lower>randint:
              print(f"The number is LOWER than {higher_lower}")
            elif higher_lower<randint:
              print(f"The number is HIGHER than {higher_lower}")
