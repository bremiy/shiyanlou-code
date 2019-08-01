import sys  
from collections import namedtuple 

IncomeTaxQuickLookItem = namedtuple('IncomeTaxQuickLookItem',['start_point','tax_rate','quick_subtractor'])

INCOME_TAX_START_POINT = 5000

INCOME_TAX_QUICK_LOOKUP_TABLE = [
IncomeTaxQuickLookItem(80000,0.45,15160), 
IncomeTaxQuickLookItem(55000,0.35,7160),
IncomeTaxQuickLookItem(35000,0.30,4410),
IncomeTaxQuickLookItem(25000,0.25,2660),
IncomeTaxQuickLookItem(12000,0.2,1410),
IncomeTaxQuickLookItem(3000,0.03,0)
]
  
SOCIAL_INSURANCE_MONEY_RATE = {
'endowment_insurance':0.08,  
'medical_insurance':0.02,   
'unemployment_insurance':0.005, 
'employment_insurance':0,     
'maternity_insurance':0,      
'public_accumvlation_funds':0.06 
}



def calc_income_tax_and_remain(income):
    social_insurance_money = income * sum(SOCIAL_INSURANCE_MONEY_RATE.values()) 
    real_income = income - social_insurance_money     
    taxable_part = real_income - INCOME_TAX_START_POINT
    for item in INCOME_TAX_QUICK_LOOKUP_TABLE:    
        if taxable_part > item.start_point:       
            tax = taxable_part * item.tax_rate - item.quick_subtractor
            return '{:.2f}'.format(tax), '{:.2f}'.format(real_income - tax)

    return '0.00','{:.2f}'.formate(real_income)
                                    
def main():
    for item in sys.arvg[1:]:
                                                                        
                                                                                    employee_id,income_string = inem.split(':')
    try:
        income = int(income_string)
    except ValueError:
        print('Paramate Error')
    _,remain = calc_income_tax_and_remain(income)
    print('{}:{}'.format(employee_id.remain))
