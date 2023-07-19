print("Ye Olde Keychain Shoppe")
options=("1. Add keychains to order\n2. Remove keychains from order\n3. View current order\n4. Checkout")
def add_keychains():
    global num_keychain
    num_keychain=0
    keychain=int(input(f"you have{num_keychain}.How many to add?"))
    num_keychain=num_keychain+keychain
    print(f"you now have{keychain} keychains.")
    return num_keychain

def remove_keychains(num_keychain):
    keychains=int(input(f"you have{num_keychain}.How many to remove?"))
    num_keychain=num_keychain-keychains
    print(f"you now have{num_keychain} keychains.")
    return 0


def view_order(num_keychain):
    cost=int(input("enter the cost"))
    cost1=cost*num_keychain
    print(f"you have{num_keychain}keychains.\nkeychains cost{cost} each.\ntotal cost is{cost1}")


def checkout():
    print("CHECKOUT")
    name=input("what is your name?")
    print(f"you have{num_keychain}.\nkeychain cost 10 each\n total cost is",(num_keychain*10))
    print(f"Thanks for your order,{name}")



while True:
    choice=int(input("please enter your choice"))
    if (choice==1):
        add_keychains()
    elif (choice==2):
        remove_keychains(num_keychain)
    
    elif (choice==3):
        view_order(num_keychain)
    
    elif (choice==4):
        checkout()
        break



