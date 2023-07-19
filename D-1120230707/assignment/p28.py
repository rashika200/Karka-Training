print("Ye Olde Keychain Shoppe")

sales_tax=0.0825
shipping_cost=5.00
perkeychain_shippingcost=1.00

def add_keychains():
    global num_keychain
    num_keychain=0
    print("ADD KEYCHAINS")
    keychain=int(input(f"you have{num_keychain}.How many to add?"))
    num_keychain=num_keychain+keychain
    print(f"you now have{keychain} keychains.")
    return num_keychain

def remove_keychains(num_keychain):
    print("REMOVE KEYCHAINS")
    keychains=int(input(f"you have{num_keychain}.How many to remove?"))
    num_keychain=num_keychain-keychains
    print(f"you now have{num_keychain} keychains.")
    return num_keychain


def view_order(num_keychain,sales_tax,shipping_cost,perkeychain_shippingcost):
    print("VIEW ORDER")
    cost=int(input("enter the cost"))
    cost1=cost*num_keychain
    shipping_charges=shipping_cost+(num_keychain*perkeychain_shippingcost)
    tax=cost1*sales_tax
    total_cost=num_keychain+shipping_charges+tax
    print(f"you have{num_keychain}keychains.\nkeychains cost{cost} each.\ntotal cost is{cost1}\nshipping charges{shipping_charges}\ntax on the order{tax}\ntotal cost{total_cost}")


def checkout(num_keychain,sales_tax,shipping_cost,perkeychain_shippingcost):
    print("CHECKOUT")
    name=input("what is your name?")
    cost=int(input("enter the cost"))
    cost1=cost*num_keychain
    shipping_charges=shipping_cost+(num_keychain*perkeychain_shippingcost)
    tax=cost1*sales_tax
    total_cost=num_keychain+shipping_charges+tax
    print(f"you have{num_keychain}keychains.\nkeychains cost{cost} each.\ntotal cost is{cost1}\nshipping charges{shipping_charges}\ntax on the order{tax}\ntotal cost{total_cost}")
    print(f"Thanks for your order,{name}")



while True:
    choice=int(input("please enter your choice"))
    if (choice==1):
        add_keychains()
    elif (choice==2):
        remove_keychains(num_keychain)
    
    elif (choice==3):
        view_order(num_keychain,sales_tax,shipping_cost,perkeychain_shippingcost)
    
    elif (choice==4):
        checkout(num_keychain,sales_tax,shipping_cost,perkeychain_shippingcost)
        break



