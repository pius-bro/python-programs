import random 
options = ("rock","car","pius","pilot","lorry")
player = None 
computer = random.choice(options)
running = True 
while True:
    player = None 
    computer = random.choice(options)
    
    while player not in options:
        player = input("Enter a choice:")
        print(computer)
        print(player)
        
        if player==computer:
            print("Its a tie!")
        elif player == "rock" and computer == "car":
            print("You won!")
        elif player == "pius" and computer == "pilot":
            print("You won!")
        elif player == "lorry" and computer == "rock":
            print("You won!")
        else:
            print("Your lose!")
    if not input("Enter a choice:")=="y".lower():
        running = False
        
print("---- Congratulation------")