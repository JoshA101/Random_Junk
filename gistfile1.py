print("Welcome to the program.")
input("\nPress any key to continue.")
accounts = []
account_number = 0
#All account usernames stored here
account_1_user = " "
account_2_user = " "
account_3_user = " "
account_4_user = " "
#All account passwords here
account_1_pass = " "
account_2_pass = " "
account_3_pass = " "
account_4_pass = " "

def make_account():
    print("\nPlease make an account:: ")
    if(account_1_user == " " and account_1_pass == " "):
        account_1_user = input("\nPlease input a username for account 1:: ")
        account_1_pass = input("\nPlease input a password for account 1:: ")
        account_1_name = input("\nPlease enter a name for this account:: ")
        accounts.append(account_1_name)
        account_number += 1
    elif(account_1_user != " " and account_1_pass != " "):
        if(account_2_user == " " and account_2_pass == " "):
            account_2_user = input("\nPlease input a username for account 2:: ")
            account_2_pass = input("\nPlease input a password for account 2:: ")
            account_2_name = input("\nPlease enter a name for this account:: ")
            accounts.append(account_2_name)
            account_number += 1
        elif(account_2_user != " " and account_2_pass != " "):
                if(account_3_user == " " and account_3_pass == " "):
                    account_3_user = input("\nPlease input a username for account 3:: ")
                    account_3_pass = input("\nPlease input a password for account 3:: ")
                    account_3_name = input("\nPlease enter a name for this account:: ")
                    accounts.append(account_3_name)
                    account_number += 1
                elif(account_3_user != " " and account_3_pass != " "):
                    if(account_4_user == " " and account_4_user == " "):
                        account_4_user = input("\nPlease input a username for account 4:: ")
                        account_4_pass = input("\nPlease input a password for account 4:: ")
                        account_4_name = input("\nPlease enter a name for this account:: ")
                        accounts.append(account_4_name)
                        account_number +=1
                    elif(account_4_user != " " and account_4_pass != " "):
                        print("\nAll accounts have been created.")

if(account_number == 0):
    make_account()
else:
    account_decision = input("\nWould you like to create an account or access an account already made?(Create or Access):: ").lower()
    if(account_decision == "create"):
        make_account()
        if(account_decision == "access"):
            account_choose = input("\nWhich account would you like to access? Please enter the name of the account you made. ")
            if(account_choose != account_1_name or account_choose != account_2_name or account_choose != account_3_name or account_choose != account_4_name):
                print("\nYou have not entered a valid name for an account.")
            elif(account_choose == account_1_name):
                account_1_user_check = input("\nPlease enter username for account 1:: ")
                account_1_pass_check = input("\nPlease enter password for account 1:: ")
                if(account_1_user_check != account_1_user or account_1_pass_check != account_1_pass):
                    print("\nYou have entered an invalid username/password.")
                elif(account_1_user_check == account_1_user and account_1_pass_check == account_1_pass):
                    print("\nWelcome, %s!" % account_1_name)
                elif(account_choose == account_2_name):
                    account_2_user_check = input("\nPlease enter username for account 2:: ")
                    account_2_pass_check = input("\nPlease enter password for account 2:: ")
                    if(account_2_user_check != account_2_user or account_2_pass_check != account_2_pass):
                        print("\nYou have entered an invalid username/password.")
                    elif(account_2_user_check == account_2_user and account_2_pass_check == account_2_pass):
                        print("\nWelcome, %s!" % account_2_name)        
                    elif(account_choose == account_3_name):
                        account_3_user_check = input("\nPlease enter username for account 3:: ")
                        account_3_pass_check = input("\nPlease enter password for account 3:: ")
                        if(account_3_user_check != account_3_user or account_3_pass_check != account_3_pass):
                            print("\nYou have entered an invalid username/password.")
                        elif(account_3_user_check == account_3_user and account_3_pass_check == account_3_pass):
                            print("\nWelcome, %s!" % account_3_name)        
                        elif(account_choose == account_4_name):
                            account_4_user_check = input("\nPlease enter username for account 4:: ")
                            account_4_pass_check = input("\nPlease enter password for account 4:: ")
                            if(account_4_user_check != account_4_user or account_4_pass_check != account_4_pass):
                                print("\nYou have entered an invalid username/password.")
                            elif(account_4_user_check == account_4_user and account_4_pass_check == account_4_pass):
                                print("\nWelcome, %s!" % account_4_name)

input("\nPress any key to continue.")