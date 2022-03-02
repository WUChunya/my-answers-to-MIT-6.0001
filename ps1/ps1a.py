# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 14:34:20 2022

@author: Administrator
"""

total_cost=float(input("Enter the cost of your dream home:",))
portion_saved=float(input("Enter the percent of your salary to save, as a decimal:",))
annual_salary=float(input("Enter your annual salary:",))
monthly_salary=annual_salary/12
portion_down_payment=total_cost*(1/4)
current_savings=0
r=0.04
number_of_month=0
while current_savings < portion_down_payment:
    current_savings=current_savings*(1+r/12)
    current_savings += monthly_salary*portion_saved
    number_of_month += 1
print("Number of months:",number_of_month)


