# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 20:24:43 2022

@author: Administrator
"""

annual_salary=float(input("Enter your annual salary: ",))
semi_annual_raise = 0.07
r=0.04
total_cost=1000000
down_payment=0.25
goal_saving=down_payment*total_cost
current_savings=0
low=0
high=10000
value = (low+high)//2
step = 0


while abs(current_savings - goal_saving) >= 100:
    current_savings=0
    new_annual_salary=annual_salary
    monthly_salary = new_annual_salary/12
    rate=value/10000

    for months in range(36):
        if months % 6 == 0 and months > 0:
            new_annual_salary += new_annual_salary*semi_annual_raise
        monthly_salary = new_annual_salary/12
        current_savings += monthly_salary*rate + current_savings*r/12
    if current_savings - goal_saving < 0:
            low = value
    else: 
            high = value
    value = (low+high)//2
    step += 1
    
if step > 13:
    print('It is not possible to pay the down payment in three years.')
else:
    print("Best savings rate:",rate)            
    print("Steps in bisection searc:",step)     

    
        
        
    
    
