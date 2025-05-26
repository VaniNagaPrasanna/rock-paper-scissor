import random
choices=["rock","paper","scissor"]
print("Welcome to the Rock Paper Scissor game!")
max_attempts=5
attempts=u_score=c_score=0
while attempts<max_attempts:
    secret_random=random.choice(choices)
    user_select=input("enter either rock or paper or scissor : ").lower()
    attempts+=1
    if user_select in choices:
        if (user_select=="rock" and secret_random=="scissor") or (user_select=="paper" and secret_random=="rock") or (user_select=="scissor" and secret_random=="paper"):
            u_score+=1
            print(f"{attempts}.You choose {user_select.upper()} and computer chooses {secret_random.upper()} and your score is {u_score} computer score {c_score}")
        elif user_select==secret_random:
            print(f"{attempts}.draw")
        else:
            c_score+=1
            print(f"{attempts}.You choose {user_select.upper()} and computer chooses {secret_random.upper()} and your score is {u_score} computer score {c_score}") 
    else:
        print("Wrong selection")  
if u_score>c_score:
    print("You Win!")
elif u_score<c_score:
    print("You Loose!")
else:
    print("it's a draw!")