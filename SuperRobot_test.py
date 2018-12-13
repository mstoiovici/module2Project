#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 12:18:56 2018

@author: maria
"""
from SuperRobot_functions1 import *


Mari = MiniBalanceTrack("Sera", 18, 2000)

product=input("Welcome to this shop! You have a balance of 2000. What do you want to buy today? Choose from laptop, phone or smartwatch. ")
Mari.substract_from_balance(product)
Mari.check_balance()
Mari.check_balance()


Mari=LoaningShoppingAssistant("Sera","", 18, 2000)


Mari.does_shopping()


