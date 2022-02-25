from logging import shutdown
import sys
import time
from traceback import print_tb
from numpy import dtype
import numpy.random as npr
import os
class Atm:
    def __init__(self):
        npr.RandomState(0)
        self.owner= []
        self.bank = "wisdom bank"
        self.location ="ogbomoso"
        self.amount="0"
        self.user_input=""
        self.customer={}
        self.predict=0
        self.details()

    def details(self):
        print("welcome to "+ self.bank)
        
        time.sleep(2)
        self.mainMenu()

    def mainMenu(self):
        print(""" choose operation, Enter:
        1. To open account
        2. To transact
        3. To quit""")
        option=input(">>> ")
        if option=="1":
            self.openAcount()
        elif option=="2":
            self.login()
        elif option =="3":
            self.quit()
        else:
            print("invalid selection")
            self.mainMenu()

    def openAcount(self, value=""):
        self.acc_name = input("Enter your prefered account name >>")
        self.phone = input("Enter your phone number >>")
        while len(self.phone) != 11:
            print("Invalid phone number. Phone lenght must be 11")
            self.phone = input("Enter your phone number >>")
        self.pin = input("Enter your prefered password >> ")
        while len(self.pin) !=4 and type(self.pin) != int:
            print("Invalid pin, pin must be integer value")
            self.pin = input("Enter your prefered password >> ")
        self.acc_type= input("Enter 1 for savings, 2 for current and 3 for fixed deposit >>")
        self.acc_number = npr.randint(1000000000)
        self.balance = 0
        self.customers_details=[self.acc_name, self.pin, self.phone, self.acc_type, self.acc_number, self.balance]
        self.customer[self.acc_number] = self.customers_details
        print(self.customer)
        if value == "":
            print(self.acc_name + " welcome to " + self.bank)
            self.mainMenu()
        else:
            self.bank_detail = self.customer.get(self.acc_number)
            return self.bank_detail


    def login(self):
        self.user_acct = int(input("please enter your account number to login > "))
        user_pin = input("please enter your password to login > ")
        self.user_detail = self.customer.get(self.user_acct)
        if self.user_detail != None and user_pin == self.user_detail[1]:
            print("welcome "+ self.customer[self.user_acct][0]+ " with the account number "+ str(self.acc_number))
            self.account_type()
        else:
            print("invalid password")
            self.login()
            
    def account_type(self):
        print("""please choose account type:
        1. savings
        2. current
        3. fixed deposit""")
        option= input(">>> ")
        if option==self.customer[self.acc_number][3]:
            self.operation()
        else:
            print("invalid selection")
            self.account_type()


    def operation(self):
        print("""please enter your operation:
            1. withdraw
            2. check balance
            3. deposit
            4. airtime recharge 
            5. open an account 
            6. transfer fund
            7. pay bills 
            8. Menu""")
        option= input(">>> ")
        # time.sleep(2)
        if option =="1":
            self.withdraw()
        elif option== "2":
            self.checkBalance()
        elif option== "3":
            self.deposit()
        elif option== "4":
            self.airtimeRecharge()
        elif option== "5":
            pass
        elif option== "6":
            self.transferFund()
        elif option=="7":
            self.payBills()
        elif option== "8":
            self.mainMenu()
        else:
            print("invalid selection")
            self.operation()    

    def withdraw(self):
        amount ={1:1000, 2:2000, 3:5000, 4:10000, 5:15000, 6:20000}
        print("""please choose amount:
        1. 1000
        2. 2000
        3. 5000
        4. 10000
        5. 15000
        6. 20000
        7. other""")
        option= int(input(">>> "))
        if option > 0 and option < 7:
            if self.user_detail[5] >= amount[option]:
                print("hold on while your transaction is processing.......")
                self.user_detail[5] -= amount[option]
                time.sleep(3)
                print("please take your cash")
                time.sleep(2) 
                self.another() 
            else:
                 print("insufficient balance")
                 self.another()
        elif option == 7:
            self.amount=int(input("please enter amount"))
            if self.user_detail[5] >= self.amount:
                print("hold on while your transaction is processing.......")
                time.sleep(3)
                print("please take your cash")
                self.user_detail[5] -= self.amount 
                time.sleep(2)
            else:
                print("insufficient balance")
            self.another()
        else:
            print("Invalid selection")
            self.withdraw()

    def another(self):
        self.command= input("press 1 to perform another transaction, press 2 to quit")
        if self.command =="1":
            self.mainMenu()
        elif self.command=="2":
            time.sleep(1)
            print("thank you for banking with us")
            time.sleep(2)
            self.quit()
        else:
            print("inavlid selection")
            self.another()

    def checkBalance(self):
        print("hold on while your transaction is processing.......")
        time.sleep(2)
        print("your balance is ", self.user_detail[5])
        time.sleep(2)
        self.another()

    def deposit(self):
        self.user_detail[5] += int(input("input amount > "))
        time.sleep(2)
        print("your account has been successfully credited with", self.user_detail[5])
        time.sleep(2)
        self.d=""
        if self.d=="":
             pass
        else:
            self.another()
        
    
    def airtimeRecharge(self):
        self.num= input("Enter phone number >>")
        while len(self.num) != 11:
            print("Invalid phone number. Phone lenght must be 11")
            self.num = input("Enter your phone number >>")
        self.network= input("Enter network provider >>")
        self.amnt= int(input("Enter amount >>"))
        time.sleep(2)
        if self.user_detail[5] >= self.amnt:
            print("recharge successfull")
            self.user_detail[5] -=self.amnt
            self.another()
        else:
            print("insufficient fund")
            time.sleep(2)
            self.another()

    def transferFund(self):
        self.dAccount= input("please enter destination account number >> ")
        self.sender= input("1. Savings 2. Current>> ")
        self.amont= int(input("please enter amount >> "))
        tran_account = self.customer[self.dAccount][5]
        if self.user_detail[5] >= self.amont :
            print("hold on while your transaction is processing........")
            tran_account += self.amont
            self.user_detail[5] -= self.amont
            time.sleep(2)
            print("Transaction successful")
            time.sleep(2)
            self.another()
        else:
            print("insufficent fund")
            time.sleep(2)
            self.another()

    def payBills(self):
        print("""Enter:
        1. Transfer to your prediction game account
        2. To pay for light bill
        . To go back to main Menu""")
        option=(">>> ")
        if option=="1":
            self.prediction()
        elif option =="2":
            self.lightBill()
        elif option =="3":
            self.mainMenu()
        else:
            print("invalid selection")
            self.payBills()

    def prediction(self):
        self.payBet=int(input("Enter your prediction account>>> "))
        self.confirm=int(input("Enter your bank pin"))
        self.betAmount=int(input('Enter amount>>> '))
        if self.user_detail[5]>=self.betAmount and self.confirm==self.user_detail[1]:
            self.user_detail[5]-= self.betAmount
            print(self.betAmount)
            return self.betAmount
        else:
            return "insufficient Fund"

    def quit(self):
        print("thanks for banking with us")
        time.sleep(1)
        sys.exit()

# atm = Atm()
