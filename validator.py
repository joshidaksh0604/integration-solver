import re

def validate_exp(exp):
    exp=exp.replace(' ','')
    if exp == '':
        return False, 'Epression cannot be empty.'
    #pattern for vaild polynomial
    term=r'(?:\d+\*?x(?:\^\d+)?|x(?:\^\d+)?|\d+)'
    
    pattern= rf'^[+-]?{term}(?:[+-]{term})*$'
    
    if re.fullmatch(pattern, exp):
        return True, 'Valid expression.'
    else:
        return False, 'Invalid polynomial expression.'