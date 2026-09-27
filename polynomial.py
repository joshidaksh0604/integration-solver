def basic_polynomial(a):
    for i in a:
        i[1]= i[1]+1 #n+1 
        i[0]= i[0]/i[1]
    return a
    