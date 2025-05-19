
def authentication(username,password):

    with open("login-credentials.txt","r") as file:
        lines=file.readlines()


    for line in lines:
        stored_name, stored_password = line.strip().split("-")
        if stored_name == username and stored_password == password:
            print("Login successful")
            return True
        else:
             return False   

def check_balance(balance):
    return balance

def deposit_money(money,balance):
        balance+=money

        return balance


def withdraw_money(money,balance):
    if money>balance:
          print("insufficient balance ")
    else:     
        balance-=money
        print("balance=",balance)
    return balance


print("Welcome to Simple ATM")
username=input("enter your username:-")
password=input("enter the password:-")

if  authentication(username,password):
      balance=1000
      while True:
            print("1.check balance")
            print("2.Deposit Money")
            print("3.Withdraw Money")
            print("4.Exit")

            choice=int(input("enter your choice:-"))

            if choice == 1:
                print("your available balance:-₹",check_balance(balance))

            elif choice == 2:
                money=int(input("how much money you want to deposit:-"))
                balance=deposit_money(money,balance)
                print("balance after deposited money:-₹",balance)
    
            elif choice==3:
                 money=int(input("enter amount for withdrawal:-"))
                 balance=withdraw_money(money,balance)
                 print("balance after withdrawal money:-₹",balance)

            elif choice ==4:
                print("Thank you for using Simple ATM. Goodbye!")
                break

            else:
                 print("invalid choice")
