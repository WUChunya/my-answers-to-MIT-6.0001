# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 15:40:24 2022

@author: Administrator
"""
annual_salary=float(input("Enter your annual salary:",))
portion_saved=float(input("Enter the percent of your salary to save, as a decimal:",))
total_cost=float(input("Enter the cost of your dream home:",))
semi_annual_raise=float(input("Enter the semi­annual raise, as a decimal:",))

monthly_salary=annual_salary/12
portion_down_payment=total_cost*(1/4)
current_savings=0
r=0.04
number_of_month=0

while current_savings < portion_down_payment:
    current_savings = current_savings*(1+r/12)
    current_savings += monthly_salary*portion_saved
    number_of_month += 1
    if number_of_month%6 == 0:
        annual_salary += annual_salary*semi_annual_raise
        monthly_salary=annual_salary/12
print("Number of months:",number_of_month)