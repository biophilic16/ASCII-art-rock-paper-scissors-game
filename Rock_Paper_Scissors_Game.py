import random 

user_points=0
comp_points=0

chances=["rock","paper","scissors"]
print("\nROCK PAPER SCISSORS GAME")
print("---------------------------")

while True:
    user_choice=input("Enter your choice rock/paper/scissors or q to quit: ").lower()
    if user_choice=='q':
        break
    if user_choice in chances:
        comp_choice=random.choice(chances)
        if user_choice=="scissors" and comp_choice=="rock":
            print("""comp_choice->Rock
                _______                        _______
            ---'   ____)                  ____(____   '--- 
                    (_____)             (______
                    (_____)             (__________
                    (____)                 (____)
            ---.__(___)                     (___)__.---
""")
        if user_choice=="scissors" and comp_choice=="scissors":
            print("""comp_choice->Scissors
              _______                         _______
          ---'   ____)____               ____(____    '--- 
                    ______)             (______
                __________)             (__________
              (____)                        (____)
        ---.__(___)                          (___)__.---
""")
        if user_choice=="scissors" and comp_choice=="paper":
            print("""comp_choice->Paper
          _______                                _______
      ---'   ____)____                      ____(____   '--- 
                ______)                   (______
                _______)                  (__________
               _______)                        (____)
      ---.__________)                            (___)__.---
""")    
        print()        
        if user_choice=="paper" and comp_choice=="paper":
            print("""comp_choice->Paper
          _______                                _______
      ---'   ____)____                      ____(____   '--- 
                ______)                    (______
                _______)                  (_______
                _______)                   (_______
      ---.__________)                       (__________.---
""")
        if user_choice=="paper" and comp_choice=="scissors":
            print("""comp_choice->Scissors
          _______                                _______
      ---'   ____)____                      ____(____   '--- 
               _______)                    (______
            __________)                   (_______
            (____)                         (_______
      ---.__(___)                           (__________.---

                  """)
        if user_choice=="paper" and comp_choice=="rock":
            print("""comp_choice->Rock
          _______                             _______
      ---'    ____)                      ____(____   '--- 
             (_____)                   (______
             (______)                 (_______
             (_____)                   (_______
      ---.__(____)                      (__________.---
""")    
        if user_choice=="rock" and comp_choice=="rock":
            print("""comp_choice->Rock
          _______                           _______
      ---'   ____)                       __(____   '--- 
            (______)                    (______)
             (______)                  (______)
             (_____)                    (_____)
      ---.___(____)                      (____)____.---
""")    
        if user_choice=="rock" and comp_choice=="paper":
            print("""comp_choice->Paper
          _______                            _______
      ---'   ____)____                    __(____   '--- 
                ______)                  (_____)
                _______)                (______)
                _______)                 (_____)
      ---.__________)                     (____)______.---
""")    
        if user_choice=="rock" and comp_choice=="scissors":
            print("""comp_choice->Scissors
          _______                            _______
      ---'   ____)_____                   __(____   '--- 
                 ______)                 (______)
              _________)                 (______)
              (____)                      (_____)
      ---.__(___)                          (____)_____.---
""")    
             
        print()
        if user_choice=='rock' and comp_choice=='scissors':
            print("#------------------->USER WINS!\n")
            user_points+=1

        elif user_choice=='scissors' and comp_choice=='paper':
            print("#------------------->USER WINS!\n")
            user_points+=1

        elif user_choice=='paper' and comp_choice=='rock':
            print("#------------------->USER WINS!\n") 
            user_points+=1

        elif user_choice==comp_choice:
            print("#------------------->TIE! TRY AGAIN\n")   
        else:
            print("#------------------->COMPUTER WINS!\n")
            comp_points+=1   
    else:
        print("\tEnter only rock/paper/scissors!")          


print("---------------------------")
print("\nUser Points     :",user_points)
print("Computer Points :",comp_points)


if user_points>comp_points:
    print("\n\tCONGRATULATIONS YOU WON! :)")
elif user_points==comp_points:
    print("\n\tIT'S A TIE! TRY AGAIN")
else:    
    print("\n\tSORRY YOU LOOSE :(")    
print()    