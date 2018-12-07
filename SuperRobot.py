#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 12:26:10 2018

@author: maria
"""
class BalanceTrack():
    def __init__(self, name, age, balance=0):
        self.name=name
        self.age=age
        self.balance=balance
  
    def substract_from_balance(self,product):
        if product=="laptop":
            self.balance-=1020
            return self.balance
        elif product=="phone":
            self.balance-=800
            return self.balance
        elif product=="smartwatch":
            self.balance-=850
            return self.balance
        else:
            print("Sorry, we don't sell boring stuff")

    def add_loan_to_balance(self, loan_amount=0):
        self.balance+=loan_amount
        return self.balance

     
    def need_loan(self):
        if self.balance<=850:
            self.add_loan_to_balance()
            return self.balance
        else:
            print("You still have: " +str(self.balance) + " left! You can continue shopping!!")
            product=input("Choose from laptop, phone or smartwatch ")
            self.substract_from_balance(product)
           
            
        
   

Mari=BalanceTrack("Sera", 18, 2000)
product=input("Choose from laptop, phone or smartwatch ")
print(Mari.balance)
Mari.substract_from_balance(product)
print(Mari.balance)
Mari.need_loan()