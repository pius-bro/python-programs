import random 

symbols =["#","$","*"]
results =[]
for symbol in range(3):
    results.append(random.choice(symbols))
    print(results) 
def row(row):
    print("|".join(row))
def get_payout(row,bet):
    if row[0]=="#":
        return bet*4
    elif row[1]=="$":
        return bet*5
    elif row[2]=="*":
        return bet*6
    else:
        print("invalid options")
def main():
    balance = 100
    print("WELCOME TO GAMING!")
    print("SYMBOLS:# $ *")
    
    while balance > 0:
        bet = int(input("Enter btet amount:"))
        
        if bet <= 0:
            balance-=bet
            print("bet amount can't be less than zero or equal to zero!")
            continue
        elif bet > balance:
            print("Insufficient amount!")
            continue
        else:
            print("Invalid")
        
        print("spinning---\n")
        row(row)
        payout = get_payout(row,bet)
        if payout > 0:
            print("CONGRATULATIONS YOU WON A BET!")
            balance+=payout
        else:
            print("YOU LOST A BET!")
        
        