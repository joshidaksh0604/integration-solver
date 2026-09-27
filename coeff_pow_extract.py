def coeff_power(exp):

    #separating polynomial terms
    exp= exp.replace('-','|-')
    exp= exp.replace('+','|+')
    exp= exp.replace('*','')
    exp= exp.replace('^','')
    exp= exp.replace(' ','')
    terms_list=exp.split('|')
    if '' in terms_list:
        terms_list.remove('')


    #separating coefficients, variable and power and storing in a list
    coeff_pow_list=[]
    for i in terms_list:
        if 'x' in i:
            x_index=i.index('x')  
            coeff_pow_list.append([i[0:x_index],i[x_index+1:len(i)+1]])
        else:
            coeff_pow_list.append([i,'0'])


    for i in range(len(coeff_pow_list)):
        for j in range(2) :
            if coeff_pow_list[i][j]=='':
                coeff_pow_list[i][j]=1    
            elif coeff_pow_list[i][j]=='+':
                coeff_pow_list[i][j]=1
            elif coeff_pow_list[i][j] == '-':
                coeff_pow_list[i][j]=-1
            coeff_pow_list[i][j]=int(coeff_pow_list[i][j])
    return coeff_pow_list
