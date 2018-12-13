#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 12:18:34 2018

@author: maria
"""

class ShoppingAssistant(object): 
    
    def __init__(self, name,product=" ", age=0, balance=0, loans_counter=0):
        self.name=name
        self.product=product
        self.age=age
        self.balance=balance
        self.loans_counter=loans_counter
    
    def does_shopping(self):
        self.get_product()
        self.buy()
        self.check_balance()    
    
        
    def get_product(self):
        self.product=input("Hello! You have a balance of {}.\n What do you want to buy today? \n Choose from laptop, phone or smartwatch. \n ".format(self.balance))
        return self.product
        
        
    def buy(self):
        if self.product=="laptop":
            print("\n A laptop costs 1020")
            self.balance-=1020
            print("Your purchase has been successful!")
            print("Your balance is now: ",self.balance)
            return self.balance
        elif self.product=="phone":
            print("\n A phone costs 800")
            self.balance-=800
            print("Your purchase has been successful!")
            print("Your balance is now: ",self.balance)
            return self.balance
        elif self.product=="smartwatch":
            print("\n A smartwatch costs 850")
            self.balance-=850
            print("Your purchase has been successful!")
            print("Your balance is now: ",self.balance)
            return self.balance
        else:
            print("\n Sorry, we don't sell boring stuff")
    
   
            
    def check_balance(self):
        """
        if self.balance>=800:
            print("\nYou can continue shopping!!")
            self.product=input("Choose from laptop, phone or smartwatch:\n ")
            #self.get_product()
            self.buy()
            #print(self.balance)
            self.check_balance()
            return self.balance
            """
        if self.balance>=1020:
            print("\nYou can continue shopping!!")
            self.product=input("Choose from laptop, phone or smartwatch: \n ")
            #self.get_product()
            self.buy()
            #print(self.balance)
            self.check_balance()
            return self.balance
        elif self.balance>=850:
            print("\nYou can continue shopping!!")
            self.product=input("Choose from phone or smartwatch: \n ")
            #self.get_product()
            self.buy()
            #print(self.balance)
            self.check_balance()
            return self.balance
        elif self.balance>=800:
            print("\nYou can continue shopping!!")
            self.product=input("Your balance will be enough to buy a phone. Please type phone if you want to buy one:\n ")
            #self.get_product()
            self.buy()
            #print(self.balance)
            self.check_balance()
            return self.balance
        
        else:
            print("\n You don't have enough balance for shopping!You will receive a loan of 1000!!")
            self.give_loan()
            self.loans_counter+=1
            self.give_loan()
            return self.loans_counter
            
        
    
class LoaningShoppingAssistant(ShoppingAssistant):
 
     def give_loan(self,loan_amount=1000):
        
        if self.loans_counter==0:
            self.balance+=loan_amount
            #print(self.balance)
            print("\n You now have: " +str(self.balance) + "! You can continue shopping!!")
            self.product=input("Choose from laptop, phone or smartwatch: \n ")
            self.buy()
            #self.check_balance()
            return self.balance
        else:
            #print("\n You now have only ",self.balance)
            print("\n You don't have enough balance to continue your shopping! \n You're not entitled to another loan yet.  Please pay your previous loan first!")

 
     
 ##############take the check_balance to the subclass and make another main function in subclass that you'll call in the tests      
     
    
        
        
   
