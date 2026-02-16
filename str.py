is_wake = True
cart =[]
while is_wake:
    if is_wake==True: 
     action = input("Enter the action to be taken!:")
     if action =='q':
        break 

     if action.isalpha():
         cart.append(action)
         for action in cart:
             print(action,end="")
             print()
print(cart)

print("💕💕😍💖😉Remember💖💖😉😉")
         
    