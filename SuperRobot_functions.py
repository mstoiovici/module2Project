#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 12:18:34 2018

@author: maria
"""

class BalanceTrack():
    def __init__(self, name, age=0, balance=0, loan_taken=0):
        self.name=name
        self.age=age
        self.balance=balance
        self.loan_taken = loan_taken
  
    def substract_from_balance(self,product):
        
        if product=="laptop":
            print("A laptop is 1020")
            self.balance-=1020
            #print(self.balance)
            return self.balance
        elif product=="phone":
            print("A phone is 800")
            self.balance-=800
            #print(self.balance)
            return self.balance
        elif product=="smartwatch":
            print("A smartwatch is 850")
            self.balance-=850
            #print(self.balance)
            return self.balance
        else:
            print("Sorry, we don't sell boring stuff")
    
   
            
    def check_balance(self):
        if self.balance>=800:
            print("You still have: " +str(self.balance) + " left! You can continue shopping!!")
            product=input("Choose from laptop, phone or smartwatch ")
            self.substract_from_balance(product)
            #print(self.balance)
            return self.balance
        else:
            print("You now  have only: " +str(self.balance) + " left! You will receive a loan of 1000!!")
            self.add_loan_to_balance()
            self.loan_taken+=1
            self.add_loan_to_balance()
            return self.loan_taken
            
        
    
class MiniBalanceTrack(BalanceTrack):
 
     def add_loan_to_balance(self,loan_amount=1000):
        
        if self.loan_taken==0:
            self.balance+=loan_amount
            #print(self.balance)
            print("You now have: " +str(self.balance) + " left! You can continue shopping!!")
            product=input("Choose from laptop, phone or smartwatch ")
            self.substract_from_balance(product)
             
            return self.balance
        else:
            print("You now have only ",self.balance)
            print("If don't have enough balance and you already had a loan you can't continue your shopping! Please pay your loan first!")
        
       
     
    
        
        
   
