import sys
from anyio import sleep
import numpy.random as np
import time
import atm
class Gamble:
    def __init__(self):
        np.RandomState(0)
        self.customer=[]
        self.company="wisdom's prediction center"
        self.location= "ogbomoso"
        self.customer={}
        self.details()

    def details(self):
        print('welcome to', self.company, self.location)
        time.sleep(2)
        print("stake and stand a chance to win double the amount !!!")
        time.sleep(2)
        self.mainMenu()

    def mainMenu(self):
        print("""choose operation, press 
        1. To create account
        2. For operation
        3. quit""")
        option= input(">>> ")
        if option == "1":
            self.createAccount()
        elif option=="2":
            self.login()
        elif option =="3":
            time.sleep(2)
            sys.exit()

    def createAccount(self, value=""):
        self.name=input('Enter fullname>> ')
        self.phone=input('Enter your phone number')
        while len(self.phone) != 11:
            print("Invalid phone number. Phone length must be 11")
            self.phone = input("Enter your phone number >>")    
        self.password=input('enter preferred password>> ')
        while len(self.password) < 4:
            print("password length must not be less than 4 ")
            self.password=input('enter preferred password>> ')
        self.account_num= np.randint(100000000)
        self.balance=0
        self.customer_details=[self.name, self.phone,self.password,self.balance]
        self.customer[self.account_num]=self.customer_details
        print("Registration successfull !!!")
        time.sleep(2)
        # print("your details are ", self.customer)
        time.sleep(2)
        print("Redirecting to create bank account.......")
        time.sleep(3)
        atm.Atm.openAcount(self, "from betGame")
        time.sleep(2)
        print("Your bank account is empty, you need to make a deposit")
        self.deposit()
        print("Redirecting to prediction game........")
        time.sleep(3)
        print(self.name + " welcome to "+ self.company)
        time.sleep(2)
        self.another()

    def another(self):
        option=input("press 1 to login or 2 to go back to main menu>> ")
        if option=="1":
            time.sleep(2)
            self.login()
        elif option=="2":
            time.sleep(2)
            self.mainMenu()
        else:
            print("invalid selection")
            time.sleep(2)
            self.another()

    def login(self):
        self.user_details=self.customer[self.account_num]
        self.user=input("Enter username>> ")
        self.pin=input("Enter password>> ")
        if self.user_details[0]== self.user and self.user_details[2]==self.pin:
            self.operation()
        else:
            print("invalid login details")
            self.login()

    def operation(self):
        print("""please choose operation:
        1. credit account
        2. predict
        3. check balance
        4. withdraw money to bank account
        5 . Go to main menu""")
        option=input(">>> ")
        if option=="1":
            self.fundAcount()
        elif option=="3":
            self.checkAcc_balance()
        elif option=="4":
            self.withdraw()
        elif option=="5":
            self.mainMenu()
        elif option=="2":
            self.play()

        else:
            print("invalid selcetion")
            self.operation()

    def replay(self):
        option=input("Enter 1 to replay or 2 to go back to main menu>> ")
        if option=="1":
            self.play()
        elif option=="2":
            self.mainMenu()
        else:
            print("invalid selection")
            self.replay()

    def deposit(self):
        self.amount = int(input("Enter your amount >> "))
        self.pwd=input("Enter your bank pin")
        if self.bank_detail[1]==self.pwd:
            self.bank_detail[5] += self.amount
            time.sleep(2)
            print("You have successfully credited account with ", self.amount)
            time.sleep(2)
            print("Redirecting to prediction game.......")
            time.sleep(3)
            self.mainMenu()
        else:
            print("wrong password")
            self.deposit()

    def withdraw(self):
        self.withd=int(input("Enter amount you wish to send to bank account"))
        self.user_details[3]-= self.withd
        self.bank_detail[5]+= self.withd
        self.operation()

    def fundAcount(self):
        self.betAmount = int(input("Enter the amount >> "))
        self.p=input("Enter bank pin")
        if self.bank_detail[5] >= self.betAmount and self.bank_detail[1]==self.p:
           self.bank_detail[5] -=self.betAmount
           self.user_details[3] += self.betAmount
           self.operation()
        else:
            print("Insufficient fund")
        self.operation()
    
    def play(self):
        print("""Choose task, press :
        1. To play at the range of 1 - 9 (10000 - unlimited)
        2. To play at the range of 1 - 99(1000 - 9999)
        3. To play at the range of 1 - 999(100 - 999)
        4. To play at the range of 1 - 9999(5 - 99)
        5. To go to operation """)
        option=input(">>> ")
        if option=="1":
            self.bAmount()
        elif option=="2":
            self.mAmount()
        elif option=="3":
            self.sAmount()
        elif option=="4":
            self.eSmallAmount()
        elif option=="5":
            self.operation()
        else:
            print("invalid selection")
            self.operation()

    def bAmount(self):
        self.result= np.randint(1, 10)
        self.value=int(input("please enter your prediction value from 1 to 9>>  "))
        self.bet=int(input("Enter stake>> "))
        time.sleep(2)
        if self.bet <=self.user_details[3] and self.bet >=10000 :
            self.user_details[3]-=self.bet
            if self.result==self.value:
                print("Congratulations you have sucessfully won and your account has been credited with double your stake" )
                time.sleep(2)
                self.user_details[3]+=self.bet *2
                self.replay()
            else:
                print("you lost, please try again !!!")
                print("the result is ", self.result)
                time.sleep(2)
                self.replay()
        else:
            print("insufficient fund")
            time.sleep(2)
            self.replay()

    def mAmount(self):
        self.result= np.randint(1, 100)
        self.value=int(input("please enter your prediction value from 1 to 99>>  "))
        self.bet=int(input("Enter stake>> "))
        time.sleep(2)
        if self.bet <=self.user_details[3] and self.bet >= 1000 and self.bet <=9999 :
            self.user_details[3]-=self.bet
            if self.result==self.value:
                print("Congratulations you have sucessfully won and your account has been credited with double your stake" )
                time.sleep(2)
                self.user_details[3]+=self.bet *2
                self.replay()
            else:
                print("you lost, please try again !!!")
                print("the result is ", self.result)
                time.sleep(2)
                self.replay()
        else:
            print("insufficient fund")
            time.sleep(2)
            self.replay()

    def sAmount(self):
        self.result= np.randint(1, 1000)
        self.value=int(input("please enter your prediction value from 1 to 999>>  "))
        self.bet=int(input("Enter stake>> "))
        time.sleep(2)
        if self.bet <=self.user_details[3] and self.bet <1000 and self.bet >=999 :
            self.user_details[3]-=self.bet
            if self.result==self.value:
                print("Congratulations you have sucessfully won and your account has been credited with double your stake" )
                time.sleep(2)
                self.user_details[3]+=self.bet *2
                self.replay()
            else:
                print("you lost, please try again !!!")
                print("the result is ", self.result)
                time.sleep(2)
                self.replay()
        else:
            print("insufficient fund")
            time.sleep(2)
            self.replay()

    def eSmallAmount(self):
        self.result= np.randint(1, 10000)
        self.value=int(input("please enter your prediction value from 1 to 9999>>  "))
        self.bet=int(input("Enter stake>> "))
        time.sleep(2)
        if self.bet <=self.user_details[3] and self.bet >=5 and self.bet <=99 :
            self.user_details[3]-=self.bet
            if self.result==self.value:
                print("Congratulations you have sucessfully won and your account has been credited with double your stake" )
                time.sleep(2)
                self.user_details[3]+=self.bet *2
                self.replay()
            else:
                print("you lost, please try again !!!")
                print("the result is ", self.result)
                time.sleep(2)
                self.replay()
        else:
            print("insufficient fund")
            time.sleep(2)
            self.replay()




    def checkAcc_balance(self):
        print("your balance is ", self.user_details[3])
        self.another()

gb = Gamble()