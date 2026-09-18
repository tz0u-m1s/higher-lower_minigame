from random import randint
from time import sleep
times_played=0
diff=0

while True:
    start_game=input("Start playing Higher/Lower? (Y/N)")

    if start_game=="Y" or start_game=="y":
      while diff<1 or diff>3:
        try:
         diff=int(input("Select Difficulty (1,2,3) "))

         if diff<1 or diff>3:
           print("Try again!")
           continue
         
         
        except ValueError:
            print('oops, try again!')
            continue
        
        
        print("Starting game...")
        randnum=randint(1,3)
        sleep(1)
        print("Picking Number...")
        sleep(2)
        print("All done!")
        sleep(1)
        print("\n"*15)
        if diff==1:
           print("You have: 20 questions")
           question_amount=1
           while question_amount<=20:
            print("\n"*3)
            question=int(input(f"Ask question no.{question_amount} Type 1 to see if it is higher or lower than a number you choose,\n2 if you want to see an area of where the number is,\n3 if you want to see if the number is odd or even(+2 questions) ,\nand 4 if you want to guess"))
            if question==1:

               higher_lower=int(input("Select a number to see if the secret number is higher or lower than it: "))
               if higher_lower>randnum:
                  print(f"The number is LOWER than {higher_lower}")
                  question_amount+=1
                  sleep(1)
               elif higher_lower<randnum:
                  print(f"The number is HIGHER than {higher_lower}")
                  question_amount+=1
                  sleep(1)
               else:
                  print(f"You found it in {question_number} guesses!")
                  exit()
                  
            elif question==2:
               if  randnum<24:
                  areanum1=0
                  areanum2=randnum+randint(10,24)
               else:
                  areanum1=randnum-randint(10,24)
                  areanum2=randnum+randint(10,24)
               print(f'The secret number is between{areanum1}-{areanum2}')
               sleep(1)
               question_amount+=1
            elif question==3:
               if randnum%2==0.0:
                  print("The number is EVEN")
                  sleep(1)
                  question_amount+=2
               else:
                  print("The number is ODD")
                  sleep(1)
                  question_amount+=2
            elif question==4:         
               guess=int(input("Type in your guess:\n"))
               if guess==randnum:
                  print(f"You found it in {question_number} guesses!")
                  exit()

           print("You have no guesses left, you lost!")       
           exit() 

        if diff==2:
           print("You have: 15 questions")
           question_amount=1
           while question_amount<=15:
            print("\n"*15)
      
            question=int(input(f"Ask question no.{question_amount} Type 1 to see if it is higher or lower than a number you choose,\n2 if you want to see an area of where the number is,\n3 if you want to see if the number is odd or even(+2 questions) ,\nand 4 if you want to guess"))
            if question==1:

               higher_lower=int(input("Select a number to see if the secret number is higher or lower than it: "))
               if higher_lower>randnum:
                  print(f"The number is LOWER than {higher_lower}")
                  question_amount+=1
                  sleep(1.5)
               elif higher_lower<randnum:
                  print(f"The number is HIGHER than {higher_lower}")
                  question_amount+=1
                  sleep(1.5)
               else:
                  print(f"You found it in {question_number} guesses!")
                  exit()
                  
            elif question==2:
               if  randnum<24:
                  areanum1=0
                  areanum2=randnum+randint(10,24)
               else:
                  areanum1=randnum-randint(10,24)
                  areanum2=randnum+randint(10,24)
               print(f'The secret number is between{areanum1}-{areanum2}')
               sleep(1)
               question_amount+=1
            elif question==3:
               if randnum%2==0.0:
                  print("The number is EVEN")
                  question_amount+=2
               else:
                  print("The number is ODD")
                  question_amount+=2
            elif question==4:         
               guess=int(input("Type in your guess:\n"))
               if guess==randnum:
                  print(f"You found it in {question_number} guesses!")
                  exit()
           print("You have no guesses left, you lost!")
           exit()       
        if diff==3:
           print("You have: 10 questions")
           question_amount=1
           while question_amount<=10:
            print("\n"*15)
     
            question=int(input(f"Ask question no.{question_amount} Type 1 to see if it is higher or lower than a number you choose,\n2 if you want to see an area of where the number is,\n3 if you want to see if the number is odd or even(+2 questions) ,\nand 4 if you want to guess"))
            if question==1:

               higher_lower=int(input("Select a number to see if the secret number is higher or lower than it: "))
               if higher_lower>randnum:
                  print(f"The number is LOWER than {higher_lower}")
                  question_amount+=1
                  sleep(1.5)
               elif higher_lower<randnum:
                  print(f"The number is HIGHER than {higher_lower}")
                  question_amount+=1
                  sleep(1.5)
               else:
                  print(f"You found it in {question_number} guesses!")
                  exit()
                  
            elif question==2:
               if  randnum<24:
                  areanum1=0
                  areanum2=randnum+randint(10,24)
               else:
                  areanum1=randnum-randint(10,24)
                  areanum2=randnum+randint(10,24)
               print(f'The secret number is between{areanum1}-{areanum2}')
               sleep(1)
               question_amount+=1
            elif question==3:
               if randnum%2==0.0:
                  print("The number is EVEN")
                  sleep(1)
                  question_amount+=2
               else:
                  print("The number is ODD")
                  sleep(1)
                  question_amount+=2
            elif question==4:         
               guess=int(input("Type in your guess:\n"))
               if guess==randnum:
                  print(f"You found it in {question_number} guesses!")
                  exit()
           print("You have no guesses left, you lost!")       
           exit()       
       
         
         