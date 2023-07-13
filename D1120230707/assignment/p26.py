print("Ye Olde Keychain Shoppe")
options=("1. Add keychains to order\n2. Remove keychains from order\n3. View current order\n4. Checkout")
def add_keychain():
    print("ADD KEYCHAINS\n",options)
    



def remove_keychain():
    print ("REMOVE KEYCHAINS\n",options)




def view_order():
    
    print ("VIEW ORDER\n",options)




def checkout():
    print ("CHECKOUT")




choice=int(input("please enter your choice: "))
if (choice==1):
    add_keychain()
elif (choice==2):
    remove_keychain()
    
elif (choice==3):
    view_order()
    
elif (choice==4):
    checkout()
    
    

