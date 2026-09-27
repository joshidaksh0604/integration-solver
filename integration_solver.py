import polynomial as poly
import coeff_pow_extract as extract
import output_construct as answer
import validator as valid


#take input as exp from the user
exp=input('enter your expression in terms of x : ')



#checking valid entry 
is_valid, message=valid.validate_exp(exp)

if is_valid:
    #separating the coeff and power form the terms
    coeff_pow_list=extract.coeff_power(exp)

    #integrating and storing updated coefficients and powers in the list
    poly.basic_polynomial(coeff_pow_list)

    #constructing output
    answer.output(coeff_pow_list) 

else:
    print('You gave invalid character')

