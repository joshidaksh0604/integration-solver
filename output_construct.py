def output(coeff_pow_list):
    for i in coeff_pow_list:
        if i[1]==0 and i[0]==1:
            print(f'+{int(i[0])}', end='')
        elif i[1]==0 and i[0]==-1:
            print(f'{int(i[0])}', end='')
        elif i[1]==1 and i[0]==1:
            print(f'+x', end='')
        elif i[1]==1 and i[0]==-1:
            print(f'-x', end='')
        elif i[1]==0:
            if i[0]<0:
                print(f'{int(i[0])}', end='')
            elif i[0]>0:
                print(f'+{int(i[0])}', end='')    
            else:        
                pass
        elif i[1]==1:
            if i[0]<0:
                print(f'{int(i[0])}x', end='')
            elif i[0]>0:
                print(f'+{int(i[0])}x', end='')
            else:
                pass
        elif i[1]>1:
            if i[0]<0:
                print(f'{i[0]:.1f}x^{int(i[1])}', end='')
            elif i[0]>0:
                print(f'+{i[0]:.1f}x^{int(i[1])}', end='')    
            else:        
                pass
        elif int(i[0])==0:
            print('+0', end='')
        else:
            print(f'+{int(i[0])}x^{int(i[1])}', end='')