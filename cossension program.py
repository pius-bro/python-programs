# menu

menu= {"pizza":15,
        "beef" :20,
        "snacks":30,
        "soda":50,
        "lemode":30,
        "nyam":100,
        "guarana":200}
cart = []
total = 0
for key,value in menu.items():
    print(f"{key:10} Ksh.{value}")
while True:
    food = input("Enter the food (q to quit):").lower()
    if food =="q":
        break 
    elif menu.get(food):
        cart.append(food)
for food in cart:
    total += menu.get(food)
    print(food,end="")
    print()
print(f"Total is {total}")

    