# console based ATM
users = {'62433570421':['Reena', 3000,1234],
         '62433570422':['John',10000,9087],
         '62433570423':['Alex', 4000, 1122],
         '62433570424':['Michael', 1000,9988],
         '62433570425':['Lilly', 2000, 3366]
         }
print('**************WELCOME TO ATM **************')
print()
acc_no = input('Please enter your account number: ')
if acc_no in users:
    max_attempts = 3
    attempt = 1
    while attempt < 3:
        user_pin = int(input('Please enter pin:'))
        db_pin = users[acc_no][-1]
        if user_pin != db_pin:
            rem_attempts = max_attempts - attempt
            if rem_attempts == 0:
                active = False
                print('Account locked please visit later....')
            else:
                print('Invalid Pin')
                print(f'You have {rem_attempts} attempts left')
        else:
            active = True
            print('Logged in....')
            break
        attempt += 1
    transactions = []
    while active:
        
        print('Please choose your task: ')
        print('1.WITHDRAW')
        print('2.DEPOSIT')
        print('3.BALANCE ENQUIRY')
        print('4.PIN CHANGE')
        print('5.MINI STATEMENT')
        print('6.EXIT')
        choice = int(input('Enter your choice Number: '))
        if choice == 1:
            amount = int(input('please enter the amount for withdraw:'))
            in_balance = users[acc_no][1]
            if amount <= in_balance:
                u_pin = int(input('please enter your pin: '))
                if u_pin == users[acc_no][-1]:
                    users[acc_no][1] -= amount
                    tra = f'{amount} withdrawn'
                    transactions.append(tra)
                    print('Amount Withdrawn')
                else:
                    print('Wrong pin')
                
            else:
                print('Insufficient funds')
                

        elif choice == 2:
            amount = int(input('please enter amount for deposit:'))
            if amount > 0:
                users[acc_no][1] += amount
                tra = f'{amount} Deposit'
                transactions.append(tra)
                print('Deposited successfully')
            else:
                print('Invalid amount')

        elif choice == 3:
            balance = users[acc_no][1]
            print(f'Current balance: {balance}')

        elif choice == 4:
            curr_pin = int(input('Enter Your Current PIN: '))
            db_pin = users[acc_no][-1]
            if curr_pin == db_pin:
                new_pin = int(input('Enter Your New PIN: '))
                c_pin = int(input('Please Confirm the pin: '))
                if new_pin == c_pin:
                    users[acc_no][-1] = new_pin
                    print('PIN Changed Successfully')
                else:
                    print('PIN verification Failed')

        elif choice == 5:
            print("--------------MINI STATEMENT ---------------")
            if len(transactions) <= 3:
                mini_stat = transactions[::-1]
            else:
                mini_stat = transactions[-1:-4:-1]
            for i in mini_stat:
                print(i)
                print()
            

        elif choice == 6:
            print('*******THANK YOU *******')
            break
        else:
            print("Invalid Choice")
        
        
                   
 

else:
    print('Account does not exist')

    
    
