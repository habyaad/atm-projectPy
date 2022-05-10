###     ABC Bank Of Nigeria     ###
### Author's Name: Ade Omotosho
### Time: 4 sittings(An average of 12 hours in total)

    ### Welcome Message ###
print('Welcome to ABC Bank of Nigeria')

### Check  number of trials ###
trials = 3

    ### Customer's Details ###
accountNumber = int(input('Enter Your Account Number[10 digits]: '))
pin = int(input('Input your transaction pin[5 digits]: '))

### Verification ###

while len(str(accountNumber)) != 10 or len(str(pin)) != 5:   ### Can't check length of an integer, so it has to be converted to string first.
    trials = trials - 1
    if trials == 2:
        print(f'Invalid account details, you have {trials} trials left')
        accountNumber = input('Enter Your Account Number[10 digits]: ')
        pin = input('Input your transaction pin[5 digits]: ')

    elif trials == 1:
        print(f'Invalid account details, you have {trials} trial left')
        accountNumber = input('Enter Your Account Number[10 digits]: ')
        pin = input('Input your transaction pin[5 digits]: ')

    elif trials == 0:
        print('You have entered incorrect details three times, therefore banned from using our service temporarily')
        break


if len(str(accountNumber)) == 10 and len(str(pin)) == 5:
    balance = int(input('How much do you have in your ABC BANK dummy account(1,000 - 1,000,000): '))
    while balance < 1000 or balance > 1000000:
        print('Your dummy account balance must not be lesser than 1000 naira or greater than 1,000,000 naira')
        balance = int(input('How much do you have in your ABC BANK dummy account(1,000 - 1,000,000): '))

### Main Menu ###

    print('MAIN MENU')
    print('1 - View My Balance \n2 - Withdraw Cash \n3 - Funds Transaction \n4 - Exit')

    operation = input('Select an operation to be carried out: ')

### Error Check ###

    while operation != '1' and operation != '2' and operation != '3' and operation != '4' :
        print('you have not made a correct choice')
        operation = input('Select an operation to be carried out: ')

### Check account balance ###

    if operation == '1':
        print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')

### Withdrawal Menu ###

    elif operation == '2':
        
        print('WITHDRAWAL MENU\n')
        print('1 - 1000 \t4 - 10,000 \n2 - 2000 \t5 - Enter an amount \n3 - 5000 \t6 - Cancel transaction ')
        withdrawal_choice = input('Choose a withdrawal amount: ')
        while withdrawal_choice != '1' and withdrawal_choice != '2' and withdrawal_choice != '3' and withdrawal_choice != '4' and withdrawal_choice != '5' and withdrawal_choice != '6':
            print('You have not entered a correct selection')
            withdrawal_choice = input('Choose a withdrawal amount: ')
        
    ### withdraw 1000 ###

        if withdrawal_choice == '1':
            if balance >= 1000:
                balance = balance - 1000
                print('Dear Customer, you withdrew 1,000 naira from your ABC BANK dummy account')
                print(f'You have {balance} naira in your ABC BANK dummy account')

            else:
                print('Dear Customer, your account balance is not sufficient to carry out this operation')
                print(f'You have {balance} naira in your ABC BANK dummy account')
        
    ### withdraw 2000 ###
        
        elif withdrawal_choice == '2':
            if balance >= 2000:
                balance = balance - 2000
                print('Dear Customer, you withdrew 2,000 naira from your ABC BANK dummy account')
                print(f'You have {balance} naira in your ABC BANK dummy account')

            else:
                print('Dear Customer, your account balance is not sufficient to carry out this operation')
                print(f'You have {balance} naira in your ABC BANK dummy account')

    ### withdraw 5000 ###

        elif withdrawal_choice == '3':
            if balance >= 5000:
                balance = balance - 5000
                print('Dear Customer, you withdrew 5,000 naira from your ABC BANK dummy account')
                print(f'You have {balance} naira in your ABC BANK dummy account')

            else:
                print('Dear Customer, your account balance is not sufficient to carry out this operation')
                print(f'You have {balance} naira in your ABC BANK dummy account')

    ### withdraw 10000 ###

        elif withdrawal_choice == '4':
            if balance >= 10000:
                balance = balance - 10000
                print('Dear Customer, you withdrew 10,000 naira from your ABC BANK dummy account')
                print(f'You have {balance} naira in your ABC BANK dummy account')

            else:
                print('Dear Customer, your account balance is not sufficient to carry out this operation')
                print(f'You have {balance} naira in your ABC BANK dummy account')

    ### withdraw a specific amount ###

        elif withdrawal_choice == '5':
            amount = int(input('Enter the amount you want to withdraw: '))
            while amount < 0 or amount > balance:
                print('You can not withdraw less than 0 naira or more than your account balance')
                amount = int(input('Enter the amount you want to withdraw: '))

            if balance >= amount and amount >= 0:
                balance = balance - amount
                print(f'Dear Customer, you withdrew {amount} naira from your ABC BANK dummy account')
                print(f'You have {balance} naira in your ABC BANK dummy account')

            else:
                print('Dear Customer, your account balance is not sufficient to carry out this operation')
                print(f'You have {balance} naira in your ABC BANK dummy account')

    ### Cancel withdrawal transaction ###

        elif withdrawal_choice == '6':
            cancel = input('Do you want to cancel transaction(Y/N): ')

    ### Confirm cancellation of withdrawal

            while cancel != "n" and cancel != "N" and cancel != "Y" and cancel != "y":
                print("You've not selected a correct option")
                cancel = input('Do you want to cancel transaction(Y/N): ')

    ### If No to cancellation, reshow the withdrawal menu ###

            while cancel == 'n' or cancel == 'N':
                print('WITHDRAWAL MENU\n')
                print('1 - 1000 \t4 - 10,000 \n2 - 2000 \t5 - Enter an amount \n3 - 5000 \t6 - Cancel transaction ')
                withdrawal_choice = input('Choose a withdrawal amount: ')
                if withdrawal_choice == '1':
                    if balance >= 1000:
                        balance = balance - 1000
                        print('Dear Customer, you withdrew 1000 naira from your ABC BANK dummy account')
                        print(f'You have {balance} naira in your ABC BANK dummy account')
                        break
                    else:
                        print('Dear Customer, your account balance is not sufficient to carry out this operation')
                        print(f'You have {balance} naira in your ABC BANK dummy account')
                        break
                elif withdrawal_choice == '2':
                    if balance >= 2000:
                        balance = balance - 2000
                        print('Dear Customer, you withdrew 2000 naira from your ABC BANK dummy account')
                        print(f'You have {balance} naira in your ABC BANK dummy account')
                        break

                    else:
                        print('Dear Customer, your account balance is not sufficient to carry out this operation')
                        print(f'You have {balance} naira in your ABC BANK dummy account')
                        break
                elif withdrawal_choice == '3':
                    if balance >= 5000:
                        balance = balance - 5000
                        print('Dear Customer, you withdrew 5000 naira from your ABC BANK dummy account')
                        print(f'You have {balance} naira in your ABC BANK dummy account')
                        break

                    else:
                        print('Dear Customer, your account balance is not sufficient to carry out this operation')
                        print(f'You have {balance} naira in your ABC BANK dummy account')
                        break
                elif withdrawal_choice == '4':
                    if balance >= 10000:
                        balance = balance - 10000
                        print('Dear Customer, you withdrew 2000 naira from your ABC BANK dummy account')
                        print(f'You have {balance} naira in your ABC BANK dummy account')
                        break

                    else:
                        print('Dear Customer, your account balance is not sufficient to carry out this operation')
                        print(f'You have {balance} naira in your ABC BANK dummy account')
                        break
                elif withdrawal_choice == '5':
                    amount = int(input('Enter the amount you want to withdraw: '))
                    while amount < 0 or amount > balance:
                        print('You can not withdraw less than 0 naira or more than your account balance')
                        amount = int(input('Enter the amount you want to withdraw: '))

                    if balance >= amount and amount >= 0:
                        balance = balance - amount
                        print(f'Dear Customer, you withdrew {amount} naira from your ABC BANK dummy account')
                        print(f'You have {balance} naira in your ABC BANK dummy account')
                        break

                    else:
                        print('Dear Customer, your account balance is not sufficient to carry out this operation')
                        print(f'You have {balance} naira in your ABC BANK dummy account')
                        break
                elif withdrawal_choice == '6':
                    cancel = input('Do you want to cancel transaction(Y/N): ')
                    while cancel != "n" and cancel != "N" and cancel != "Y" and cancel != "y":
                        print("You've not selected a correct option")
                        cancel = input('Do you want to cancel transaction(Y/N): ')

    ### If Yes to cancellation, End Transaction ###
            if cancel == 'Y' or cancel == 'y':
                print('Withdrawal Transaction Cancelled and 0 naira deducted')
                print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                print('Thanks for using ABC BANK of NIGERIA')

### Fund transaction menu ###
    elif operation == '3':
        print('FUND TRANSACTION MENU')
        print('1 - Transfer Funds \n2 - Deposit Cash \n3 - Convert Cash Currency \n4 - Exit')

### Choose what you'd like to do with your funds ###

        fund_choice = input('Select an operation to be carried out: ')

### If wrong choice ###
        while fund_choice != '1' and fund_choice != '2' and fund_choice != '3' and fund_choice != '4':
            print('you have not made a correct choice')
            fund_choice = input('Select an operation to be carried out: ')
### Transfer Funds ###
        if fund_choice == '1':    
            recipent_account_number = int(input("Enter the recipient's account number(10 digits): "))

    ### Confirm recipient's details ###

            while len(str(recipent_account_number)) != 10 :    
                print('Invalid account number')
                recipent_account_number = int(input("Enter the recipient's account number(10 digits): "))
            while recipent_account_number == accountNumber:
                print('Dear Customer, you cannot transfer money from an account to the same account ')
                recipent_account_number = int(input("Enter the recipient's account number(10 digits): "))

            transfer_amount = int(input('Input Transfer amount: '))

    ### Check the amount to be transaction

            while transfer_amount > balance or transfer_amount < 0:
                print('Your transfer amount can neither be greater than your balance nor less than 0')
                print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                transfer_amount = int(input('Input Transfer amount: '))

    ### Confirm Transfer Transaction ### 

            confirmation = input(f'Do you confirm sending {transfer_amount} naira to {recipent_account_number}?(Y/N) ')
            while confirmation != "n" and confirmation != "N" and confirmation != "Y" and confirmation != "y":
                print("You've not selected a correct option")
                confirmation = input(f'Do you confirm sending {transfer_amount} naira to {recipent_account_number}?(Y/N) ')
    
    ### If No, don't transfer ###

            if confirmation == 'n' or confirmation == 'N':
                print(f'Fund Transfer Cancelled and 0 naira was sent to {recipent_account_number}')
                print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                print('Thanks for using ABC BANK of NIGERIA')

    ### If Yes, transfer ###

            elif confirmation == 'y' or confirmation == 'Y':
                print(f'Fund Transfer Successful and {transfer_amount} naira was sent to {recipent_account_number}')
                print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                print('Thanks for using ABC BANK of NIGERIA')

### Deposit Menu ###

        elif fund_choice == '2':    
            deposit_amount = int(input('How much do you want to deposit?(Enter 0 to cancel deposit) '))
    
    ### Check Deposit Amount ###
            while deposit_amount > 1000000 or deposit_amount < 0:
                print('Dear Customer, you can not deposit less than 0 naira or more than 1,000,000 naira at a time')
                deposit_amount = int(input('How much do you want to deposit?(Enter 0 to cancel deposit) '))
            if deposit_amount == 0:
                print('Cash Deposit terminated')
                print(f'You have {balance} naira in your ABC BANK dummy account')
            else:
                balance = balance + deposit_amount
                print('Cash Deposit Successful')
                print(f'You have {balance} naira in your ABC BANK dummy account')

### Currency Converter Menu ###

        elif fund_choice == '3':   
            print('Currency Converter Menu')
            print('Choose Currency to convert cash to: ')

    ### You can convert your Nigerian Naira(NGN) to United State Dollars(USD) or Japanese Yen(JPY) or Great Britain Pound(GBP) or European Euro(EUR) or Ghana Cedis(GHC) ###

            print('1 - USD \t4 - EUR \n2 - JPY \t5 - GHC \n3 - GBP \t6 - Cancel transaction ')
            currency = input('Which currency do you want to convert your NGN to? ')
    
    ### Verify Currency to convert to ###
            while currency != '1' and currency != '2' and currency != '3' and currency != '4' and currency != '5' and currency != '6':
                print('You have not made a correct selection')
                currency = input('Which currency do you want to convert your NGN to? ')   
    
    ### NGN to USD ###
            if currency == '1':
                convert_amount = int(input('How much of your NGN do you want to convert? '))
                while convert_amount > balance or convert_amount < 0:
                    print('Your conversion amount can neither be greater than your balance nor less than 0')
                    print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                    convert_amount = int(input('How much of your NGN do you want to convert? '))
                balance = balance - convert_amount
                dollar = round(convert_amount/411.50,2)
                print(f'Conversion Successful, You now have {dollar} USD in your ABC BANK dollar account')
                print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
    
    ### NGN to JPY
            elif currency == '2':
                convert_amount = int(input('How much of your NGN do you want to convert? '))
                while convert_amount > balance or convert_amount < 0:
                    print('Your conversion amount can neither be greater than your balance nor less than 0')
                    print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                    convert_amount = int(input('How much of your NGN do you want to convert? '))
                balance = balance - convert_amount
                yen = round(convert_amount/3.71,2)
                print(f'Conversion Successful, You now have {yen} JPY in your ABC BANK japanese yen account')
                print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
    
    ### NGN to GBP ###

            elif currency == '3':
                convert_amount = int(input('How much of your NGN do you want to convert? '))
                while convert_amount > balance or convert_amount < 0:
                    print('Your conversion amount can neither be greater than your balance nor less than 0')
                    print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                    convert_amount = int(input('How much of your NGN do you want to convert? '))
                balance = balance - convert_amount
                pound = round(convert_amount/571.37,2)
                print(f'Conversion Successful, You now have {pound} GBP in your ABC BANK pound sterling account')
                print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
    
    ### NGN to EUR ###
            elif currency == '4':
                convert_amount = int(input('How much of your NGN do you want to convert? '))
                while convert_amount > balance or convert_amount < 0:
                    print('Your conversion amount can neither be greater than your balance nor less than 0')
                    print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                    convert_amount = int(input('How much of your NGN do you want to convert? '))
                balance = balance - convert_amount
                eur = round(convert_amount/491.17,2)
                print(f'Conversion Successful, You now have {eur} EUR in your ABC BANK Euro account')
                print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
    
    ### NGN to GHC ###
            elif currency == '5':
                convert_amount = int(input('How much of your NGN do you want to convert? '))
                while convert_amount > balance or convert_amount < 0:
                    print('Your conversion amount can neither be greater than your balance nor less than 0')
                    print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                    convert_amount = int(input('How much of your NGN do you want to convert? '))
                balance = balance - convert_amount
                cedis = round(convert_amount/70.46,2)
                print(f'Conversion Successful, You now have {cedis} GHC in your ABC BANK ghana cedis account')
                print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
    
    ### Cancel Currency Conversion ###

            elif currency == '6':
                currency_exit = input('do you want to cancel transaction?(Y/N) ')
                while currency_exit != "n" and currency_exit != "N" and currency_exit != "Y" and currency_exit != "y":
                    print("You've not selected a correct option")
                    currency_exit = input('Do you want to cancel transaction(Y/N): ')

        ### If No, reshow Currency Converter menu ###

                while currency_exit == 'n' or currency_exit == 'N':

                    print('Currency Converter Menu')
                    print('Choose Currency to convert cash to: ')

            ### You can convert your Nigerian Naira(NGN) to United State Dollars(USD) or Japanese Yen(JPY) or Great Britain Pound(GBP) or European Euro(EUR) or Ghana Cedis(GHC) ###

                    print('1 - USD \t4 - EUR \n2 - JPY \t5 - GHC \n3 - GBP \t6 - Cancel transaction ')
                    currency = input('Which currency do you want to convert your NGN to? ')
            
            ### Verify Currency to convert to ###
                    while currency != '1' and currency != '2' and currency != '3' and currency != '4' and currency != '5' and currency != '6':
                        print('You have not made a correct selection')
                        currency = input('Which currency do you want to convert your NGN to? ')   
            
            ### NGN to USD ###
                    if currency == '1':
                        convert_amount = int(input('How much of your NGN do you want to convert? '))
                        while convert_amount > balance or convert_amount < 0:
                            print('Your conversion amount can neither be greater than your balance nor less than 0')
                            print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                            convert_amount = int(input('How much of your NGN do you want to convert? '))
                        balance = balance - convert_amount
                        dollar = round(convert_amount/411.50,2)
                        print(f'Conversion Successful, You now have {dollar} USD in your ABC BANK dollar account')
                        print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                        break
            ### NGN to JPY
                    elif currency == '2':
                        convert_amount = int(input('How much of your NGN do you want to convert? '))
                        while convert_amount > balance or convert_amount < 0:
                            print('Your conversion amount can neither be greater than your balance nor less than 0')
                            print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                            convert_amount = int(input('How much of your NGN do you want to convert? '))
                        balance = balance - convert_amount
                        yen = round(convert_amount/3.71,2)
                        print(f'Conversion Successful, You now have {yen} JPY in your ABC BANK japanese yen account')
                        print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                        break
            
            ### NGN to GBP ###

                    elif currency == '3':
                        convert_amount = int(input('How much of your NGN do you want to convert? '))
                        while convert_amount > balance or convert_amount < 0:
                            print('Your conversion amount can neither be greater than your balance nor less than 0')
                            print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                            convert_amount = int(input('How much of your NGN do you want to convert? '))
                        balance = balance - convert_amount
                        pound = round(convert_amount/571.37,2)
                        print(f'Conversion Successful, You now have {pound} GBP in your ABC BANK pound sterling account')
                        print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                        break
            
            ### NGN to EUR ###
                    elif currency == '4':
                        convert_amount = int(input('How much of your NGN do you want to convert? '))
                        while convert_amount > balance or convert_amount < 0:
                            print('Your conversion amount can neither be greater than your balance nor less than 0')
                            print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                            convert_amount = int(input('How much of your NGN do you want to convert? '))
                        balance = balance - convert_amount
                        eur = round(convert_amount/491.17,2)
                        print(f'Conversion Successful, You now have {eur} EUR in your ABC BANK Euro account')
                        print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                        break
            
            ### NGN to GHC ###
                    elif currency == '5':
                        convert_amount = int(input('How much of your NGN do you want to convert? '))
                        while convert_amount > balance or convert_amount < 0:
                            print('Your conversion amount can neither be greater than your balance nor less than 0')
                            print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                            convert_amount = int(input('How much of your NGN do you want to convert? '))
                        balance = balance - convert_amount
                        cedis = round(convert_amount/70.46,2)
                        print(f'Conversion Successful, You now have {cedis} GHC in your ABC BANK ghana cedis account')
                        print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                        break
            
            ### Cancel Currency Conversion ###

                    elif currency == '6':
                        currency_exit = input('do you want to cancel transaction?(Y/N) ')
                        while currency_exit != "n" and currency_exit != "N" and currency_exit != "Y" and currency_exit != "y":
                            print("You've not selected a correct option")
                            currency_exit = input('Do you want to cancel transaction(Y/N): ')


        ### If Yes, End process ###
                if currency_exit == 'Y' or currency_exit == 'y':
                    print('Currency Conversion Cancelled')
                    print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                    print('Thanks for using ABC BANK of NIGERIA')

### Exit Fund Transaction Menu
        elif fund_choice == '4':    
            fund_exit = input('Confirm that you want to quit transaction(Y/N): ')
            while fund_exit != "n" and fund_exit != "N" and fund_exit != "Y" and fund_exit != "y":
                print("You've not selected a correct option")
                fund_exit = input('Confirm that you want to quit transaction(Y/N): ')

    ### If No, reshow Fund transaction menu ###

            while fund_exit == 'n' or fund_exit == 'N':
                print('FUND TRANSACTION MENU')
                print('1 - Transfer Funds \n2 - Deposit Cash \n3 - Convert Cash Currency \n4 - Exit')

        ### Choose what you'd like to do with your funds ###

                fund_choice = input('Select an operation to be carried out: ')

        ### If wrong choice ###
                while fund_choice != '1' and fund_choice != '2' and fund_choice != '3' and fund_choice != '4':
                    print('you have not made a correct choice')
                    fund_choice = input('Select an operation to be carried out: ')
        ### Transfer Funds ###
                if fund_choice == '1':    
                    recipent_account_number = int(input("Enter the recipient's account number(10 digits): "))

            ### Confirm recipient's details ###

                    while len(str(recipent_account_number)) != 10 :    
                        print('Invalid account number')
                        recipent_account_number = int(input("Enter the recipient's account number(10 digits): "))
                    while recipent_account_number == accountNumber:
                        print('Dear Customer, you cannot transfer money from an account to the same account ')
                        recipent_account_number = int(input("Enter the recipient's account number(10 digits): "))

                    transfer_amount = int(input('Input Transfer amount: '))

            ### Check the amount to be transaction

                    while transfer_amount > balance or transfer_amount < 0:
                        print('Your transfer amount can neither be greater than your balance nor less than 0')
                        print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                        transfer_amount = int(input('Input Transfer amount: '))

            ### Confirm Transfer Transaction ### 

                    confirmation = input(f'Do you confirm sending {transfer_amount} naira to {recipent_account_number}?(Y/N) ')
                    while confirmation != "n" and confirmation != "N" and confirmation != "Y" and confirmation != "y":
                        print("You've not selected a correct option")
                        confirmation = input(f'Do you confirm sending {transfer_amount} naira to {recipent_account_number}?(Y/N) ')
            
            ### If No, don't transfer ###

                    if confirmation == 'n' or confirmation == 'N':
                        print(f'Fund Transfer Cancelled and 0 naira was sent to {recipent_account_number}')
                        print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                        print('Thanks for using ABC BANK of NIGERIA')
                        break
            ### If Yes, transfer ###

                    elif confirmation == 'y' or confirmation == 'Y':
                        print(f'Fund Transfer Successful and {transfer_amount} naira was sent to {recipent_account_number}')
                        print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                        print('Thanks for using ABC BANK of NIGERIA')
                        break

        ### Deposit Menu ###

                elif fund_choice == '2':    
                    deposit_amount = int(input('How much do you want to deposit?(Enter 0 to cancel deposit) '))
            
            ### Check Deposit Amount ###
                    while deposit_amount > 1000000 or deposit_amount < 0:
                        print('Dear Customer, you can not deposit less than 0 naira or more than 1,000,000 naira at a time')
                        deposit_amount = int(input('How much do you want to deposit?(Enter 0 to cancel deposit) '))
                    if deposit_amount == 0:
                        print('Cash Deposit terminated')
                        print(f'You have {balance} naira in your ABC BANK dummy account')
                        break

                    else:
                        balance = balance + deposit_amount
                        print('Cash Deposit Successful')
                        print(f'You have {balance} naira in your ABC BANK dummy account')
                        break

        ### Currency Converter Menu ###

                elif fund_choice == '3':   
                    print('Currency Converter Menu')
                    print('Choose Currency to convert cash to: ')

            ### You can convert your Nigerian Naira(NGN) to United State Dollars(USD) or Japanese Yen(JPY) or Great Britain Pound(GBP) or European Euro(EUR) or Ghana Cedis(GHC) ###

                    print('1 - USD \t4 - EUR \n2 - JPY \t5 - GHC \n3 - GBP \t6 - Cancel transaction ')
                    currency = input('Which currency do you want to convert your NGN to? ')
            
            ### Verify Currency to convert to ###
                    while currency != '1' and currency != '2' and currency != '3' and currency != '4' and currency != '5' and currency != '6':
                        print('You have not made a correct selection')
                        currency = input('Which currency do you want to convert your NGN to? ')   
            
            ### NGN to USD ###
                    if currency == '1':
                        convert_amount = int(input('How much of your NGN do you want to convert? '))
                        while convert_amount > balance or convert_amount < 0:
                            print('Your conversion amount can neither be greater than your balance nor less than 0')
                            print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                            convert_amount = int(input('How much of your NGN do you want to convert? '))
                        balance = balance - convert_amount
                        dollar = round(convert_amount/411.50,2)
                        print(f'Conversion Successful, You now have {dollar} USD in your ABC BANK dollar account')
                        print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                        break
            
            ### NGN to JPY
                    elif currency == '2':
                        convert_amount = int(input('How much of your NGN do you want to convert? '))
                        while convert_amount > balance or convert_amount < 0:
                            print('Your conversion amount can neither be greater than your balance nor less than 0')
                            print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                            convert_amount = int(input('How much of your NGN do you want to convert? '))
                        balance = balance - convert_amount
                        yen = round(convert_amount/3.71,2)
                        print(f'Conversion Successful, You now have {yen} JPY in your ABC BANK japanese yen account')
                        print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                        break
            
            ### NGN to GBP ###

                    elif currency == '3':
                        convert_amount = int(input('How much of your NGN do you want to convert? '))
                        while convert_amount > balance or convert_amount < 0:
                            print('Your conversion amount can neither be greater than your balance nor less than 0')
                            print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                            convert_amount = int(input('How much of your NGN do you want to convert? '))
                        balance = balance - convert_amount
                        pound = round(convert_amount/571.37,2)
                        print(f'Conversion Successful, You now have {pound} GBP in your ABC BANK pound sterling account')
                        print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                        break
            
            ### NGN to EUR ###
                    elif currency == '4':
                        convert_amount = int(input('How much of your NGN do you want to convert? '))
                        while convert_amount > balance or convert_amount < 0:
                            print('Your conversion amount can neither be greater than your balance nor less than 0')
                            print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                            convert_amount = int(input('How much of your NGN do you want to convert? '))
                        balance = balance - convert_amount
                        eur = round(convert_amount/491.17,2)
                        print(f'Conversion Successful, You now have {eur} EUR in your ABC BANK Euro account')
                        print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                        break
            
            ### NGN to GHC ###
                    elif currency == '5':
                        convert_amount = int(input('How much of your NGN do you want to convert? '))
                        while convert_amount > balance or convert_amount < 0:
                            print('Your conversion amount can neither be greater than your balance nor less than 0')
                            print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                            convert_amount = int(input('How much of your NGN do you want to convert? '))
                        balance = balance - convert_amount
                        cedis = round(convert_amount/70.46,2)
                        print(f'Conversion Successful, You now have {cedis} GHC in your ABC BANK ghana cedis account')
                        print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                        break
            
            ### Cancel Currency Conversion ###

                    elif currency == '6':
                        currency_exit = input('do you want to cancel transaction?(Y/N) ')
                        while currency_exit != "n" and currency_exit != "N" and currency_exit != "Y" and currency_exit != "y":
                            print("You've not selected a correct option")
                            currency_exit = input('Do you want to cancel transaction(Y/N): ')

                ### If No, reshow Currency Converter menu ###

                        while currency_exit == 'n' or currency_exit == 'N':

                            print('Currency Converter Menu')
                            print('Choose Currency to convert cash to: ')

                    ### You can convert your Nigerian Naira(NGN) to United State Dollars(USD) or Japanese Yen(JPY) or Great Britain Pound(GBP) or European Euro(EUR) or Ghana Cedis(GHC) ###

                            print('1 - USD \t4 - EUR \n2 - JPY \t5 - GHC \n3 - GBP \t6 - Cancel transaction ')
                            currency = input('Which currency do you want to convert your NGN to? ')
                    
                    ### Verify Currency to convert to ###
                            while currency != '1' and currency != '2' and currency != '3' and currency != '4' and currency != '5' and currency != '6':
                                print('You have not made a correct selection')
                                currency = input('Which currency do you want to convert your NGN to? ')   
                    
                    ### NGN to USD ###
                            if currency == '1':
                                convert_amount = int(input('How much of your NGN do you want to convert? '))
                                while convert_amount > balance or convert_amount < 0:
                                    print('Your conversion amount can neither be greater than your balance nor less than 0')
                                    print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                                    convert_amount = int(input('How much of your NGN do you want to convert? '))
                                balance = balance - convert_amount
                                dollar = round(convert_amount/411.50,2)
                                print(f'Conversion Successful, You now have {dollar} USD in your ABC BANK dollar account')
                                print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                                break

                    ### NGN to JPY
                            elif currency == '2':
                                convert_amount = int(input('How much of your NGN do you want to convert? '))
                                while convert_amount > balance or convert_amount < 0:
                                    print('Your conversion amount can neither be greater than your balance nor less than 0')
                                    print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                                    convert_amount = int(input('How much of your NGN do you want to convert? '))
                                balance = balance - convert_amount
                                yen = round(convert_amount/3.71,2)
                                print(f'Conversion Successful, You now have {yen} JPY in your ABC BANK japanese yen account')
                                print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                                break
                    
                    ### NGN to GBP ###

                            elif currency == '3':
                                convert_amount = int(input('How much of your NGN do you want to convert? '))
                                while convert_amount > balance or convert_amount < 0:
                                    print('Your conversion amount can neither be greater than your balance nor less than 0')
                                    print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                                    convert_amount = int(input('How much of your NGN do you want to convert? '))
                                balance = balance - convert_amount
                                pound = round(convert_amount/571.37,2)
                                print(f'Conversion Successful, You now have {pound} GBP in your ABC BANK pound sterling account')
                                print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                                break
                    
                    ### NGN to EUR ###
                            elif currency == '4':
                                convert_amount = int(input('How much of your NGN do you want to convert? '))
                                while convert_amount > balance or convert_amount < 0:
                                    print('Your conversion amount can neither be greater than your balance nor less than 0')
                                    print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                                    convert_amount = int(input('How much of your NGN do you want to convert? '))
                                balance = balance - convert_amount
                                eur = round(convert_amount/491.17,2)
                                print(f'Conversion Successful, You now have {eur} EUR in your ABC BANK Euro account')
                                print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                                break
                    
                    ### NGN to GHC ###
                            elif currency == '5':
                                convert_amount = int(input('How much of your NGN do you want to convert? '))
                                while convert_amount > balance or convert_amount < 0:
                                    print('Your conversion amount can neither be greater than your balance nor less than 0')
                                    print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                                    convert_amount = int(input('How much of your NGN do you want to convert? '))
                                balance = balance - convert_amount
                                cedis = round(convert_amount/70.46,2)
                                print(f'Conversion Successful, You now have {cedis} GHC in your ABC BANK ghana cedis account')
                                print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                                break
                    
                    ### Cancel Currency Conversion ###

                            elif currency == '6':
                                currency_exit = input('do you want to cancel transaction?(Y/N) ')
                                while currency_exit != "n" and currency_exit != "N" and currency_exit != "Y" and currency_exit != "y":
                                    print("You've not selected a correct option")
                                    currency_exit = input('Do you want to cancel transaction(Y/N): ')


                ### If Yes, End process ###
                        if currency_exit == 'Y' or currency_exit == 'y':
                            print('Currency Conversion Cancelled')
                            print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                            print('Thanks for using ABC BANK of NIGERIA')
                        
                        break
        ### Exit Fund Transaction Menu
                elif fund_choice == '4':    
                    fund_exit = input('Confirm that you want to quit transaction(Y/N): ')
                    while fund_exit != "n" and fund_exit != "N" and fund_exit != "Y" and fund_exit != "y":
                        print("You've not selected a correct option")
                        fund_exit = input('Confirm that you want to quit transaction(Y/N): ')

    ### If Yes, Exit Fund transaction menu###

            if fund_exit == 'y' or fund_exit == 'Y':
                print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                print('Thanks for using ABC BANK of NIGERIA')

### Quit Operation
    elif operation == '4':
        confirm_exit = input('Do you want to terminate operation(Y/N): ')
        while confirm_exit != "n" and confirm_exit != "N" and confirm_exit != "Y" and confirm_exit != "y":
            print("You've not selected a correct option")
            confirm_exit = input('Do you want to terminate operation(Y/N): ')

    ### If No, reshow Main Menu ###
        while confirm_exit == 'n' or confirm_exit == 'N':
            
            print('MAIN MENU')
            print('1 - View My Balance \n2 - Withdraw Cash \n3 - Funds Transaction \n4 - Exit')

            operation = input('Select an operation to be carried out: ')

        ### Error Check ###

            while operation != '1' and operation != '2' and operation != '3' and operation != '4' :
                print('you have not made a correct choice')
                operation = input('Select an operation to be carried out: ')

        ### Check account balance ###

            if operation == '1':
                print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                break
        ### Withdrawal Menu ###

            elif operation == '2':
                
                print('WITHDRAWAL MENU\n')
                print('1 - 1000 \t4 - 10,000 \n2 - 2000 \t5 - Enter an amount \n3 - 5000 \t6 - Cancel transaction ')
                withdrawal_choice = input('Choose a withdrawal amount: ')
                while withdrawal_choice != '1' and withdrawal_choice != '2' and withdrawal_choice != '3' and withdrawal_choice != '4' and withdrawal_choice != '5' and withdrawal_choice != '6':
                    print('You have not entered a correct selection')
                    withdrawal_choice = input('Choose a withdrawal amount: ')
                
            ### withdraw 1000 ###

                if withdrawal_choice == '1':
                    if balance >= 1000:
                        balance = balance - 1000
                        print('Dear Customer, you withdrew 1,000 naira from your ABC BANK dummy account')
                        print(f'You have {balance} naira in your ABC BANK dummy account')

                    else:
                        print('Dear Customer, your account balance is not sufficient to carry out this operation')
                        print(f'You have {balance} naira in your ABC BANK dummy account')
                
            ### withdraw 2000 ###
                
                elif withdrawal_choice == '2':
                    if balance >= 2000:
                        balance = balance - 2000
                        print('Dear Customer, you withdrew 2,000 naira from your ABC BANK dummy account')
                        print(f'You have {balance} naira in your ABC BANK dummy account')

                    else:
                        print('Dear Customer, your account balance is not sufficient to carry out this operation')
                        print(f'You have {balance} naira in your ABC BANK dummy account')

            ### withdraw 5000 ###

                elif withdrawal_choice == '3':
                    if balance >= 5000:
                        balance = balance - 5000
                        print('Dear Customer, you withdrew 5,000 naira from your ABC BANK dummy account')
                        print(f'You have {balance} naira in your ABC BANK dummy account')

                    else:
                        print('Dear Customer, your account balance is not sufficient to carry out this operation')
                        print(f'You have {balance} naira in your ABC BANK dummy account')

            ### withdraw 10000 ###

                elif withdrawal_choice == '4':
                    if balance >= 10000:
                        balance = balance - 10000
                        print('Dear Customer, you withdrew 10,000 naira from your ABC BANK dummy account')
                        print(f'You have {balance} naira in your ABC BANK dummy account')

                    else:
                        print('Dear Customer, your account balance is not sufficient to carry out this operation')
                        print(f'You have {balance} naira in your ABC BANK dummy account')

            ### withdraw a specific amount ###

                elif withdrawal_choice == '5':
                    amount = int(input('Enter the amount you want to withdraw: '))
                    while amount < 0 or amount > balance:
                        print('You can not withdraw less than 0 naira or more than your account balance')
                        amount = int(input('Enter the amount you want to withdraw: '))

                    if balance >= amount and amount >= 0:
                        balance = balance - amount
                        print(f'Dear Customer, you withdrew {amount} naira from your ABC BANK dummy account')
                        print(f'You have {balance} naira in your ABC BANK dummy account')

                    else:
                        print('Dear Customer, your account balance is not sufficient to carry out this operation')
                        print(f'You have {balance} naira in your ABC BANK dummy account')

            ### Cancel withdrawal transaction ###

                elif withdrawal_choice == '6':
                    cancel = input('Do you want to cancel transaction(Y/N): ')

            ### Confirm cancellation of withdrawal

                    while cancel != "n" and cancel != "N" and cancel != "Y" and cancel != "y":
                        print("You've not selected a correct option")
                        cancel = input('Do you want to cancel transaction(Y/N): ')

            ### If No to cancellation, reshow the withdrawal menu ###

                    while cancel == 'n' or cancel == 'N':
                        print('WITHDRAWAL MENU\n')
                        print('1 - 1000 \t4 - 10,000 \n2 - 2000 \t5 - Enter an amount \n3 - 5000 \t6 - Cancel transaction ')
                        withdrawal_choice = input('Choose a withdrawal amount: ')
                        if withdrawal_choice == '1':
                            if balance >= 1000:
                                balance = balance - 1000
                                print('Dear Customer, you withdrew 1000 naira from your ABC BANK dummy account')
                                print(f'You have {balance} naira in your ABC BANK dummy account')
                                break
                            else:
                                print('Dear Customer, your account balance is not sufficient to carry out this operation')
                                print(f'You have {balance} naira in your ABC BANK dummy account')
                                break
                        elif withdrawal_choice == '2':
                            if balance >= 2000:
                                balance = balance - 2000
                                print('Dear Customer, you withdrew 2000 naira from your ABC BANK dummy account')
                                print(f'You have {balance} naira in your ABC BANK dummy account')
                                break

                            else:
                                print('Dear Customer, your account balance is not sufficient to carry out this operation')
                                print(f'You have {balance} naira in your ABC BANK dummy account')
                                break
                        elif withdrawal_choice == '3':
                            if balance >= 5000:
                                balance = balance - 5000
                                print('Dear Customer, you withdrew 5000 naira from your ABC BANK dummy account')
                                print(f'You have {balance} naira in your ABC BANK dummy account')
                                break

                            else:
                                print('Dear Customer, your account balance is not sufficient to carry out this operation')
                                print(f'You have {balance} naira in your ABC BANK dummy account')
                                break
                        elif withdrawal_choice == '4':
                            if balance >= 10000:
                                balance = balance - 10000
                                print('Dear Customer, you withdrew 2000 naira from your ABC BANK dummy account')
                                print(f'You have {balance} naira in your ABC BANK dummy account')
                                break

                            else:
                                print('Dear Customer, your account balance is not sufficient to carry out this operation')
                                print(f'You have {balance} naira in your ABC BANK dummy account')
                                break
                        elif withdrawal_choice == '5':
                            amount = int(input('Enter the amount you want to withdraw: '))
                            while amount < 0 or amount > balance:
                                print('You can not withdraw less than 0 naira or more than your account balance')
                                amount = int(input('Enter the amount you want to withdraw: '))

                            if balance >= amount and amount >= 0:
                                balance = balance - amount
                                print(f'Dear Customer, you withdrew {amount} naira from your ABC BANK dummy account')
                                print(f'You have {balance} naira in your ABC BANK dummy account')
                                break

                            else:
                                print('Dear Customer, your account balance is not sufficient to carry out this operation')
                                print(f'You have {balance} naira in your ABC BANK dummy account')
                                break
                        elif withdrawal_choice == '6':
                            cancel = input('Do you want to cancel transaction(Y/N): ')
                            while cancel != "n" and cancel != "N" and cancel != "Y" and cancel != "y":
                                print("You've not selected a correct option")
                                cancel = input('Do you want to cancel transaction(Y/N): ')

            ### If Yes to cancellation, End Transaction ###
                    if cancel == 'Y' or cancel == 'y':
                        print('Withdrawal Transaction Cancelled and 0 naira deducted')
                        print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                        print('Thanks for using ABC BANK of NIGERIA')
                break
        ### Fund transaction menu ###
            elif operation == '3':
                print('FUND TRANSACTION MENU')
                print('1 - Transfer Funds \n2 - Deposit Cash \n3 - Convert Cash Currency \n4 - Exit')
        
            ### Choose what you'd like to do with your funds ###

                fund_choice = input('Select an operation to be carried out: ')

            
        ### If wrong choice ###
                while fund_choice != '1' and fund_choice != '2' and fund_choice != '3' and fund_choice != '4':
                    print('you have not made a correct choice')
                    fund_choice = input('Select an operation to be carried out: ')
                    
            ### Transfer Funds ###
                if fund_choice == '1':    
                    recipent_account_number = int(input("Enter the recipient's account number(10 digits): "))

            ### Confirm recipient's details ###

                    while len(str(recipent_account_number)) != 10 :    
                        print('Invalid account number')
                        recipent_account_number = int(input("Enter the recipient's account number(10 digits): "))
                    while recipent_account_number == accountNumber:
                        print('Dear Customer, you cannot transfer money from an account to the same account ')
                        recipent_account_number = int(input("Enter the recipient's account number(10 digits): "))

                    transfer_amount = int(input('Input Transfer amount: '))

            ### Check the amount to be transaction

                    while transfer_amount > balance or transfer_amount < 0:
                        print('Your transfer amount can neither be greater than your balance nor less than 0')
                        print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                        transfer_amount = int(input('Input Transfer amount: '))

            ### Confirm Transfer Transaction ### 

                    confirmation = input(f'Do you confirm sending {transfer_amount} naira to {recipent_account_number}?(Y/N) ')
                    while confirmation != "n" and confirmation != "N" and confirmation != "Y" and confirmation != "y":
                        print("You've not selected a correct option")
                        confirmation = input(f'Do you confirm sending {transfer_amount} naira to {recipent_account_number}?(Y/N) ')
            
            ### If No, don't transfer ###

                    if confirmation == 'n' or confirmation == 'N':
                        print(f'Fund Transfer Cancelled and 0 naira was sent to {recipent_account_number}')
                        print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                        print('Thanks for using ABC BANK of NIGERIA')

            ### If Yes, transfer ###

                    elif confirmation == 'y' or confirmation == 'Y':
                        print(f'Fund Transfer Successful and {transfer_amount} naira was sent to {recipent_account_number}')
                        print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                        print('Thanks for using ABC BANK of NIGERIA')

            ### Deposit Menu ###

                elif fund_choice == '2':    
                    deposit_amount = int(input('How much do you want to deposit?(Enter 0 to cancel deposit) '))
            
            ### Check Deposit Amount ###
                    while deposit_amount > 1000000 or deposit_amount < 0:
                        print('Dear Customer, you can not deposit less than 0 naira or more than 1,000,000 naira at a time')
                        deposit_amount = int(input('How much do you want to deposit?(Enter 0 to cancel deposit) '))
                    if deposit_amount == 0:
                        print('Cash Deposit terminated')
                        print(f'You have {balance} naira in your ABC BANK dummy account')
                    else:
                        balance = balance + deposit_amount
                        print('Cash Deposit Successful')
                        print(f'You have {balance} naira in your ABC BANK dummy account')

            ### Currency Converter Menu ###

                elif fund_choice == '3':   
                    print('Currency Converter Menu')
                    print('Choose Currency to convert cash to: ')

            ### You can convert your Nigerian Naira(NGN) to United State Dollars(USD) or Japanese Yen(JPY) or Great Britain Pound(GBP) or European Euro(EUR) or Ghana Cedis(GHC) ###

                    print('1 - USD \t4 - EUR \n2 - JPY \t5 - GHC \n3 - GBP \t6 - Cancel transaction ')
                    currency = input('Which currency do you want to convert your NGN to? ')
            
            ### Verify Currency to convert to ###
                    while currency != '1' and currency != '2' and currency != '3' and currency != '4' and currency != '5' and currency != '6':
                        print('You have not made a correct selection')
                        currency = input('Which currency do you want to convert your NGN to? ')   
            
            ### NGN to USD ###
                    if currency == '1':
                        convert_amount = int(input('How much of your NGN do you want to convert? '))
                        while convert_amount > balance or convert_amount < 0:
                            print('Your conversion amount can neither be greater than your balance nor less than 0')
                            print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                            convert_amount = int(input('How much of your NGN do you want to convert? '))
                        balance = balance - convert_amount
                        dollar = round(convert_amount/411.50,2)
                        print(f'Conversion Successful, You now have {dollar} USD in your ABC BANK dollar account')
                        print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
            
            ### NGN to JPY
                    elif currency == '2':
                        convert_amount = int(input('How much of your NGN do you want to convert? '))
                        while convert_amount > balance or convert_amount < 0:
                            print('Your conversion amount can neither be greater than your balance nor less than 0')
                            print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                            convert_amount = int(input('How much of your NGN do you want to convert? '))
                        balance = balance - convert_amount
                        yen = round(convert_amount/3.71,2)
                        print(f'Conversion Successful, You now have {yen} JPY in your ABC BANK japanese yen account')
                        print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
            
            ### NGN to GBP ###

                    elif currency == '3':
                        convert_amount = int(input('How much of your NGN do you want to convert? '))
                        while convert_amount > balance or convert_amount < 0:
                            print('Your conversion amount can neither be greater than your balance nor less than 0')
                            print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                            convert_amount = int(input('How much of your NGN do you want to convert? '))
                        balance = balance - convert_amount
                        pound = round(convert_amount/571.37,2)
                        print(f'Conversion Successful, You now have {pound} GBP in your ABC BANK pound sterling account')
                        print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
            
            ### NGN to EUR ###
                    elif currency == '4':
                        convert_amount = int(input('How much of your NGN do you want to convert? '))
                        while convert_amount > balance or convert_amount < 0:
                            print('Your conversion amount can neither be greater than your balance nor less than 0')
                            print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                            convert_amount = int(input('How much of your NGN do you want to convert? '))
                        balance = balance - convert_amount
                        eur = round(convert_amount/491.17,2)
                        print(f'Conversion Successful, You now have {eur} EUR in your ABC BANK Euro account')
                        print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
            
            ### NGN to GHC ###
                    elif currency == '5':
                        convert_amount = int(input('How much of your NGN do you want to convert? '))
                        while convert_amount > balance or convert_amount < 0:
                            print('Your conversion amount can neither be greater than your balance nor less than 0')
                            print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                            convert_amount = int(input('How much of your NGN do you want to convert? '))
                        balance = balance - convert_amount
                        cedis = round(convert_amount/70.46,2)
                        print(f'Conversion Successful, You now have {cedis} GHC in your ABC BANK ghana cedis account')
                        print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
            
            ### Cancel Currency Conversion ###

                    elif currency == '6':
                        currency_exit = input('do you want to cancel transaction?(Y/N) ')
                        while currency_exit != "n" and currency_exit != "N" and currency_exit != "Y" and currency_exit != "y":
                            print("You've not selected a correct option")
                            currency_exit = input('Do you want to cancel transaction(Y/N): ')

                ### If No, reshow Currency Converter menu ###

                        while currency_exit == 'n' or currency_exit == 'N':

                            print('Currency Converter Menu')
                            print('Choose Currency to convert cash to: ')

                    ### You can convert your Nigerian Naira(NGN) to United State Dollars(USD) or Japanese Yen(JPY) or Great Britain Pound(GBP) or European Euro(EUR) or Ghana Cedis(GHC) ###

                            print('1 - USD \t4 - EUR \n2 - JPY \t5 - GHC \n3 - GBP \t6 - Cancel transaction ')
                            currency = input('Which currency do you want to convert your NGN to? ')
                    
                    ### Verify Currency to convert to ###
                            while currency != '1' and currency != '2' and currency != '3' and currency != '4' and currency != '5' and currency != '6':
                                print('You have not made a correct selection')
                                currency = input('Which currency do you want to convert your NGN to? ')   
                    
                    ### NGN to USD ###
                            if currency == '1':
                                convert_amount = int(input('How much of your NGN do you want to convert? '))
                                while convert_amount > balance or convert_amount < 0:
                                    print('Your conversion amount can neither be greater than your balance nor less than 0')
                                    print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                                    convert_amount = int(input('How much of your NGN do you want to convert? '))
                                balance = balance - convert_amount
                                dollar = round(convert_amount/411.50,2)
                                print(f'Conversion Successful, You now have {dollar} USD in your ABC BANK dollar account')
                                print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                                break
                    ### NGN to JPY
                            elif currency == '2':
                                convert_amount = int(input('How much of your NGN do you want to convert? '))
                                while convert_amount > balance or convert_amount < 0:
                                    print('Your conversion amount can neither be greater than your balance nor less than 0')
                                    print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                                    convert_amount = int(input('How much of your NGN do you want to convert? '))
                                balance = balance - convert_amount
                                yen = round(convert_amount/3.71,2)
                                print(f'Conversion Successful, You now have {yen} JPY in your ABC BANK japanese yen account')
                                print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                                break
                    
                    ### NGN to GBP ###

                            elif currency == '3':
                                convert_amount = int(input('How much of your NGN do you want to convert? '))
                                while convert_amount > balance or convert_amount < 0:
                                    print('Your conversion amount can neither be greater than your balance nor less than 0')
                                    print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                                    convert_amount = int(input('How much of your NGN do you want to convert? '))
                                balance = balance - convert_amount
                                pound = round(convert_amount/571.37,2)
                                print(f'Conversion Successful, You now have {pound} GBP in your ABC BANK pound sterling account')
                                print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                                break
                    
                    ### NGN to EUR ###
                            elif currency == '4':
                                convert_amount = int(input('How much of your NGN do you want to convert? '))
                                while convert_amount > balance or convert_amount < 0:
                                    print('Your conversion amount can neither be greater than your balance nor less than 0')
                                    print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                                    convert_amount = int(input('How much of your NGN do you want to convert? '))
                                balance = balance - convert_amount
                                eur = round(convert_amount/491.17,2)
                                print(f'Conversion Successful, You now have {eur} EUR in your ABC BANK Euro account')
                                print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                                break
                    
                    ### NGN to GHC ###
                            elif currency == '5':
                                convert_amount = int(input('How much of your NGN do you want to convert? '))
                                while convert_amount > balance or convert_amount < 0:
                                    print('Your conversion amount can neither be greater than your balance nor less than 0')
                                    print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                                    convert_amount = int(input('How much of your NGN do you want to convert? '))
                                balance = balance - convert_amount
                                cedis = round(convert_amount/70.46,2)
                                print(f'Conversion Successful, You now have {cedis} GHC in your ABC BANK ghana cedis account')
                                print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                                break
                    
                    ### Cancel Currency Conversion ###

                            elif currency == '6':
                                currency_exit = input('do you want to cancel transaction?(Y/N) ')
                                while currency_exit != "n" and currency_exit != "N" and currency_exit != "Y" and currency_exit != "y":
                                    print("You've not selected a correct option")
                                    currency_exit = input('Do you want to cancel transaction(Y/N): ')


                ### If Yes, End process ###
                        if currency_exit == 'Y' or currency_exit == 'y':
                            print('Currency Conversion Cancelled')
                            print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                            print('Thanks for using ABC BANK of NIGERIA')

            ### Exit Fund Transaction Menu
                elif fund_choice == '4':    
                    fund_exit = input('Confirm that you want to quit transaction(Y/N): ')
                    while fund_exit != "n" and fund_exit != "N" and fund_exit != "Y" and fund_exit != "y":
                        print("You've not selected a correct option")
                        fund_exit = input('Confirm that you want to quit transaction(Y/N): ')

            ### If No, reshow Fund transaction menu ###

                    while fund_exit == 'n' or fund_exit == 'N':
                        print('FUND TRANSACTION MENU')
                        print('1 - Transfer Funds \n2 - Deposit Cash \n3 - Convert Cash Currency \n4 - Exit')

                ### Choose what you'd like to do with your funds ###

                        fund_choice = input('Select an operation to be carried out: ')


                ### If wrong choice ###
                        while fund_choice != '1' and fund_choice != '2' and fund_choice != '3' and fund_choice != '4':
                            print('you have not made a correct choice')
                            fund_choice = input('Select an operation to be carried out: ')
                            
                ### Transfer Funds ###
                        if fund_choice == '1':    
                            recipent_account_number = int(input("Enter the recipient's account number(10 digits): "))

                    ### Confirm recipient's details ###

                            while len(str(recipent_account_number)) != 10 :    
                                print('Invalid account number')
                                recipent_account_number = int(input("Enter the recipient's account number(10 digits): "))
                            while recipent_account_number == accountNumber:
                                print('Dear Customer, you cannot transfer money from an account to the same account ')
                                recipent_account_number = int(input("Enter the recipient's account number(10 digits): "))

                            transfer_amount = int(input('Input Transfer amount: '))

                    ### Check the amount to be transferred

                            while transfer_amount > balance or transfer_amount < 0:
                                print('Your transfer amount can neither be greater than your balance nor less than 0')
                                print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                                transfer_amount = int(input('Input Transfer amount: '))

                    ### Confirm Transfer Transaction ### 

                            confirmation = input(f'Do you confirm sending {transfer_amount} naira to {recipent_account_number}?(Y/N) ')
                            while confirmation != "n" and confirmation != "N" and confirmation != "Y" and confirmation != "y":
                                print("You've not selected a correct option")
                                confirmation = input(f'Do you confirm sending {transfer_amount} naira to {recipent_account_number}?(Y/N) ')
                    
                    ### If No, don't transfer ###

                            if confirmation == 'n' or confirmation == 'N':
                                print(f'Fund Transfer Cancelled and 0 naira was sent to {recipent_account_number}')
                                print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                                print('Thanks for using ABC BANK of NIGERIA')
                                break
                    ### If Yes, transfer ###

                            elif confirmation == 'y' or confirmation == 'Y':
                                print(f'Fund Transfer Successful and {transfer_amount} naira was sent to {recipent_account_number}')
                                print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                                print('Thanks for using ABC BANK of NIGERIA')
                                break

                ### Deposit Menu ###

                        elif fund_choice == '2':    
                            deposit_amount = int(input('How much do you want to deposit?(Enter 0 to cancel deposit) '))
                    
                    ### Check Deposit Amount ###
                            while deposit_amount > 1000000 or deposit_amount < 0:
                                print('Dear Customer, you can not deposit less than 0 naira or more than 1,000,000 naira at a time')
                                deposit_amount = int(input('How much do you want to deposit?(Enter 0 to cancel deposit) '))
                            if deposit_amount == 0:
                                print('Cash Deposit terminated')
                                print(f'You have {balance} naira in your ABC BANK dummy account')
                                break

                            else:
                                balance = balance + deposit_amount
                                print('Cash Deposit Successful')
                                print(f'You have {balance} naira in your ABC BANK dummy account')
                                break

                ### Currency Converter Menu ###

                        elif fund_choice == '3':   
                            print('Currency Converter Menu')
                            print('Choose Currency to convert cash to: ')

                    ### You can convert your Nigerian Naira(NGN) to United State Dollars(USD) or Japanese Yen(JPY) or Great Britain Pound(GBP) or European Euro(EUR) or Ghana Cedis(GHC) ###

                            print('1 - USD \t4 - EUR \n2 - JPY \t5 - GHC \n3 - GBP \t6 - Cancel transaction ')
                            currency = input('Which currency do you want to convert your NGN to? ')
                    
                    ### Verify Currency to convert to ###
                            while currency != '1' and currency != '2' and currency != '3' and currency != '4' and currency != '5' and currency != '6':
                                print('You have not made a correct selection')
                                currency = input('Which currency do you want to convert your NGN to? ')   
                    
                    ### NGN to USD ###
                            if currency == '1':
                                convert_amount = int(input('How much of your NGN do you want to convert? '))
                                while convert_amount > balance or convert_amount < 0:
                                    print('Your conversion amount can neither be greater than your balance nor less than 0')
                                    print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                                    convert_amount = int(input('How much of your NGN do you want to convert? '))
                                balance = balance - convert_amount
                                dollar = round(convert_amount/411.50,2)
                                print(f'Conversion Successful, You now have {dollar} USD in your ABC BANK dollar account')
                                print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                                break
                    
                    ### NGN to JPY
                            elif currency == '2':
                                convert_amount = int(input('How much of your NGN do you want to convert? '))
                                while convert_amount > balance or convert_amount < 0:
                                    print('Your conversion amount can neither be greater than your balance nor less than 0')
                                    print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                                    convert_amount = int(input('How much of your NGN do you want to convert? '))
                                balance = balance - convert_amount
                                yen = round(convert_amount/3.71,2)
                                print(f'Conversion Successful, You now have {yen} JPY in your ABC BANK japanese yen account')
                                print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                                break
                    
                    ### NGN to GBP ###

                            elif currency == '3':
                                convert_amount = int(input('How much of your NGN do you want to convert? '))
                                while convert_amount > balance or convert_amount < 0:
                                    print('Your conversion amount can neither be greater than your balance nor less than 0')
                                    print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                                    convert_amount = int(input('How much of your NGN do you want to convert? '))
                                balance = balance - convert_amount
                                pound = round(convert_amount/571.37,2)
                                print(f'Conversion Successful, You now have {pound} GBP in your ABC BANK pound sterling account')
                                print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                                break
                    
                    ### NGN to EUR ###
                            elif currency == '4':
                                convert_amount = int(input('How much of your NGN do you want to convert? '))
                                while convert_amount > balance or convert_amount < 0:
                                    print('Your conversion amount can neither be greater than your balance nor less than 0')
                                    print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                                    convert_amount = int(input('How much of your NGN do you want to convert? '))
                                balance = balance - convert_amount
                                eur = round(convert_amount/491.17,2)
                                print(f'Conversion Successful, You now have {eur} EUR in your ABC BANK Euro account')
                                print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                                break
                    
                    ### NGN to GHC ###
                            elif currency == '5':
                                convert_amount = int(input('How much of your NGN do you want to convert? '))
                                while convert_amount > balance or convert_amount < 0:
                                    print('Your conversion amount can neither be greater than your balance nor less than 0')
                                    print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                                    convert_amount = int(input('How much of your NGN do you want to convert? '))
                                balance = balance - convert_amount
                                cedis = round(convert_amount/70.46,2)
                                print(f'Conversion Successful, You now have {cedis} GHC in your ABC BANK ghana cedis account')
                                print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                                break
                    
                    ### Cancel Currency Conversion ###

                            elif currency == '6':
                                currency_exit = input('do you want to cancel transaction?(Y/N) ')
                                while currency_exit != "n" and currency_exit != "N" and currency_exit != "Y" and currency_exit != "y":
                                    print("You've not selected a correct option")
                                    currency_exit = input('Do you want to cancel transaction(Y/N): ')

                        ### If No, reshow Currency Converter menu ###

                                while currency_exit == 'n' or currency_exit == 'N':

                                    print('Currency Converter Menu')
                                    print('Choose Currency to convert cash to: ')

                            ### You can convert your Nigerian Naira(NGN) to United State Dollars(USD) or Japanese Yen(JPY) or Great Britain Pound(GBP) or European Euro(EUR) or Ghana Cedis(GHC) ###

                                    print('1 - USD \t4 - EUR \n2 - JPY \t5 - GHC \n3 - GBP \t6 - Cancel transaction ')
                                    currency = input('Which currency do you want to convert your NGN to? ')
                            
                            ### Verify Currency to convert to ###
                                    while currency != '1' and currency != '2' and currency != '3' and currency != '4' and currency != '5' and currency != '6':
                                        print('You have not made a correct selection')
                                        currency = input('Which currency do you want to convert your NGN to? ')   
                            
                            ### NGN to USD ###
                                    if currency == '1':
                                        convert_amount = int(input('How much of your NGN do you want to convert? '))
                                        while convert_amount > balance or convert_amount < 0:
                                            print('Your conversion amount can neither be greater than your balance nor less than 0')
                                            print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                                            convert_amount = int(input('How much of your NGN do you want to convert? '))
                                        balance = balance - convert_amount
                                        dollar = round(convert_amount/411.50,2)
                                        print(f'Conversion Successful, You now have {dollar} USD in your ABC BANK dollar account')
                                        print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                                        break

                            ### NGN to JPY
                                    elif currency == '2':
                                        convert_amount = int(input('How much of your NGN do you want to convert? '))
                                        while convert_amount > balance or convert_amount < 0:
                                            print('Your conversion amount can neither be greater than your balance nor less than 0')
                                            print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                                            convert_amount = int(input('How much of your NGN do you want to convert? '))
                                        balance = balance - convert_amount
                                        yen = round(convert_amount/3.71,2)
                                        print(f'Conversion Successful, You now have {yen} JPY in your ABC BANK japanese yen account')
                                        print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                                        break
                            
                            ### NGN to GBP ###

                                    elif currency == '3':
                                        convert_amount = int(input('How much of your NGN do you want to convert? '))
                                        while convert_amount > balance or convert_amount < 0:
                                            print('Your conversion amount can neither be greater than your balance nor less than 0')
                                            print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                                            convert_amount = int(input('How much of your NGN do you want to convert? '))
                                        balance = balance - convert_amount
                                        pound = round(convert_amount/571.37,2)
                                        print(f'Conversion Successful, You now have {pound} GBP in your ABC BANK pound sterling account')
                                        print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                                        break
                            
                            ### NGN to EUR ###
                                    elif currency == '4':
                                        convert_amount = int(input('How much of your NGN do you want to convert? '))
                                        while convert_amount > balance or convert_amount < 0:
                                            print('Your conversion amount can neither be greater than your balance nor less than 0')
                                            print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                                            convert_amount = int(input('How much of your NGN do you want to convert? '))
                                        balance = balance - convert_amount
                                        eur = round(convert_amount/491.17,2)
                                        print(f'Conversion Successful, You now have {eur} EUR in your ABC BANK Euro account')
                                        print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                                        break
                            
                            ### NGN to GHC ###
                                    elif currency == '5':
                                        convert_amount = int(input('How much of your NGN do you want to convert? '))
                                        while convert_amount > balance or convert_amount < 0:
                                            print('Your conversion amount can neither be greater than your balance nor less than 0')
                                            print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                                            convert_amount = int(input('How much of your NGN do you want to convert? '))
                                        balance = balance - convert_amount
                                        cedis = round(convert_amount/70.46,2)
                                        print(f'Conversion Successful, You now have {cedis} GHC in your ABC BANK ghana cedis account')
                                        print(f'Dear customer, you have {balance} naira left in your ABC BANK dummy account')
                                        break
                            
                            ### Cancel Currency Conversion ###

                                    elif currency == '6':
                                        currency_exit = input('do you want to cancel transaction?(Y/N) ')
                                        while currency_exit != "n" and currency_exit != "N" and currency_exit != "Y" and currency_exit != "y":
                                            print("You've not selected a correct option")
                                            currency_exit = input('Do you want to cancel transaction(Y/N): ')


                        ### If Yes, End process ###
                                if currency_exit == 'Y' or currency_exit == 'y':
                                    print('Currency Conversion Cancelled')
                                    print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                                    print('Thanks for using ABC BANK of NIGERIA')
                                
                                break
                ### Exit Fund Transaction Menu
                        elif fund_choice == '4':    
                            fund_exit = input('Confirm that you want to quit transaction(Y/N): ')
                            while fund_exit != "n" and fund_exit != "N" and fund_exit != "Y" and fund_exit != "y":
                                print("You've not selected a correct option")
                                fund_exit = input('Confirm that you want to quit transaction(Y/N): ')

            ### If Yes, Exit Fund transaction menu###

                    if fund_exit == 'y' or fund_exit == 'Y':
                        print(f'Dear Customer, you have {balance} naira in your ABC BANK dummy account')
                        print('Thanks for using ABC BANK of NIGERIA')
                break
        ### Quit Operation
            elif operation == '4':
                confirm_exit = input('Do you want to terminate operation(Y/N): ')
                while confirm_exit != "n" and confirm_exit != "N" and confirm_exit != "Y" and confirm_exit != "y":
                    print("You've not selected a correct option")
                    confirm_exit = input('Do you want to terminate operation(Y/N): ')

    ### If Yes, Quit Transaction ###    
        if confirm_exit == 'Y' or confirm_exit == 'y':
            print('Thanks for using ABC BANK of NIGERIA')

### End of ABC BANK of Nigeria ATM Simulator code###