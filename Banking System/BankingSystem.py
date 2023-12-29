#declariation part
print("="*20)

customerNames= ['Jane Smith', 'Iason Jordan', 'David Morgan', 'Brain John', 'Jack Swift']
customerPins= ['0123', '2575', '7275', '2312', '5049']
customerBalances= [10000, 20000, 20000, 40000, 10000]
deposition=0
withdrawal=0
balance=0
counter_1=1
counter_2=5
i=0

#This statement below helps the program to run continuously.
while True:
    print("="*40)
    print(" -----Welcome to Bank of India------")
    print("*"*40)
    print("=<< 1.OPEN A NEW ACCOUNT         >>=")
    print("=<< 2.WITHDRAW MONEY             >>=")
    print("=<< 3.DEPOSIT MONEY              >>=")
    print("=<< 4.CHECK BALANCE              >>=")
    print("=<< 5.DELETE ACCOUNT             >>=")
    print("=<< 6.EXIT/QUIT                  >>=")
    print("*"*40)
    
    #The below statement takes the choice number from the user
    choiceNumber=input("Select your choice number from the above menu:")
    if choiceNumber=="1":
        print("choice number 1 is selected by the customer")
        #The line below will take the no.of customers from the user
        NOC=eval(input("Number of Customers:"))
        i=i+NOC
        #the if condition will restrict the number of new accounts to 5.
        if i>5:
            print("\n")
            print("Customer registration exceed reached or Customer registration too low")
            i=i-NOC
        else:
            #The while loop will run according to the no:of customers.
            while counter_1<=i:
                #These few lines will take information from customer and then append them to the list.
                name = input("Enter Fullname :")
                customerNames.append(name)
                pin = str(input("Please set pin of your choice :"))
                customerPins.append(pin)
                deposition = eval(input("Please input a value to deposit to start an account:"))
                balance = balance + deposition
                customerBalances.append(balance)
                print("\nName",end=" ")
                print(customerNames[counter_2])
                print("pin=",end=" ")
                print(customerPins[counter_2])
                print("balance=",end=" ")
                print(customerBalances[counter_2],end=" ")
                print("-/Rs")
                print("\nYour name is added to customers list")
                print("Your pin is added to customers list")
                print("Your balance is added to customers list")
                print("---New Account Added Successfully---")
                print("\n")
                print("Thank you for choosing Bank of India")
                print(customerNames[counter_2])
                counter_1 = counter_1 + 1
                counter_2 = counter_2 + 1
                print("\n")
                print("NOTE! please remember the name and pin")
                print("=======================================")
                #This statement below helps the user to go back to the start of the program (main menu)
        mainmenu = input("Please press enter key to go back to main menu to perform another function or exit...")
    elif choiceNumber=="2":
        j = 0
        print("Choice number 2 is selected by customer")
        #This while loop will prevent the user using the account if the username or pin is wrong.
        while j < 1:
            k = -1
            name=input("Please input name:")
            pin=input("Please input Pin:")
            #this while loop will keep the function running when variable k is smaller then length of the customerNames list
            while k<len(customerNames)-1:
                k=k+1
                #These two if conditions find where both the name and pin matches
                if name==customerNames[k]:
                    if pin==customerPins[k]:
                        j=j+1
                        #These few statement would show the the balance taken from the list.
                        print("Your current Balance:",end=" ")
                        print(customerBalances[k],end=" ")
                        print("-/Rs\n")
                        balance=customerBalances[k]
                        #Statement below would take the amount to withdraw from user.
                        withdrawal=eval(input("Input value to Withdraw:"))
                        #The if condition below would look weather the withdraw is greater than the balance.
                        if withdrawal>balance:
                            #this statement below would take a deposition from the customer.
                            deposition=eval(input("Insufficient Balance please deposite the amount:"))
                            #These few statements would update the value and show the balance to user.
                            balance=balance+deposition
                            print("Your Current balance:",end=" ")
                            print(balance,end=" ")
                            print("-/Rs\n")
                        else:
                            #else condition mentioned above is to withdraw if the balance is greater than the withdarw amount.

                            balance=balance-withdrawal
                            print("-\n")
                            print("----Withdraw Successfull!----")
                            #These few statement would update the balance in the list and show it to customer.
                            customerBalances[k]=balance
                            print("Your New Balance:",balance, end=" ")
                            print("-/Rs\n\n")
            if j<1:
                #The if condition above would work when the pin or the name is wrong.
                print("Your name and pin does not match!\n")
                break
                #This statement below helps the user to go back to the start of the program (main menu)
        mainmenu=input("Please press enter key to go back to main menu to perform another function or exit...")
    elif choiceNumber=="3":
        j = 0  
        print("Choice number 3 is selected by customer")
        #The while loop below would work when the pin or the username is wrong.
        while j<1:
            k = -1
            name=input("Please input name:")
            pin=input("Please input pin:")
            #The while loop below will keep the function running to find the correct user.
            while k<len(customerNames)-1:
                k=k+1
                #The two if conditions below would find whether both the pin and the name is correct.
                if name==customerNames[k]:
                    if pin==customerPins[k]:
                        j=j+1
                        #These statements below would show the customer balance and update list values according to the deposition made.
                        print("Your Curent Balance:",end=" ")
                        print(customerBalances[k],end=" ")
                        print("-/Rs")
                        balance=customerBalances[k]
                        #this statement below takes the deposition from the customer
                        deposition=eval(input("Enter the value you want to deposit:"))
                        balance=balance+deposition
                        customerBalances[k]=balance
                        print("\n")
                        print("----Deposition Successful!----")
                        print("Your new Balance: ",balance, end=" ")
                        print("-/Rs\n\n")
            if j<1:
                #The if condition above would work when the pin or the name is wrong.
                print("Your name and pin does not match!\n")
                break
                #This statement below helps the user to go back to the start of the program (main menu)
        mainmenu=input("Please press enter key to go back to main menu to perform another function or exit...")
    elif choiceNumber == "4":
        j = 0  
        print("Choice number 4 is selected by customer")
        #The while loop below would work when the pin or the username is wrong.
        while j<1:
            k = -1
            name=input("Please input name:")
            pin=input("Please input pin:")
            #The while loop below will keep the function running to find the correct user.
            while k<len(customerNames)-1:
                k=k+1
                #The two if conditions below would find whether both the pin and the name is correct.
                if name==customerNames[k]:
                    if pin==customerPins[k]:
                        j=j+1
                        #These statements below would show the customer balance and update list values according to the deposition made.
                        print("\nName",end=" ")
                        print(customerNames[k])
                        print("balance=",end=" ")
                        print(customerBalances[k],end=" ")
                        print("-/Rs")
            if j<1:
                #The if condition above would work when the pin or the name is wrong.
                print("Your name and pin does not match!\n")
                break
                #This statement below helps the user to go back to the start of the program (main menu)
        mainmenu=input("Please press enter key to go back to main menu to perform another function or exit...")
    elif choiceNumber == "5":
        j = 0  
        print("Choice number 5 is selected by customer")
        #The while loop below would work when the pin or the username is wrong.
        while j<1:
            k = -1
            name=input("Please input name:")
            pin=input("Please input pin:")
            #The while loop below will keep the function running to find the correct user.
            while k<len(customerNames)-1:
                k=k+1
                #The two if conditions below would find whether both the pin and the name is correct.
                if name==customerNames[k]:
                    if pin==customerPins[k]:
                        j=j+1
                        #These statements below will delete the account.
                        customerNames.remove(name)
                        customerPins.remove(pin)
                        print("\n")
                        print("Account has been successfully deleted")
                        print("=======================================")
                        
            if j<1:
                #The if condition above would work when the pin or the name is wrong.
                print("Your name and pin does not match!\n")
                break
                #This statement below helps the user to go back to the start of the program (main menu)
        mainmenu=input("Please press enter key to go back to main menu to perform another function or exit...")
    elif choiceNumber=="6":
        #These Statements would be just showed to the customer.
        print("Choice number 6 is selected by customer")
        print("Thank you for using our banking system!")
        print("\n")
        print("Come Again!")
        print("Bye Bye!")
        break
    else:
        #this else statement above would work when a wrong function is chosen.
        print("Invalid option selected by the Customer")
        print("Please Try Again!")
        #This statement below helps the user to go back to the start of the program (main menu)
        mainmenu=input("Please press enter key to go back to main menu to perform another function or exit...")
