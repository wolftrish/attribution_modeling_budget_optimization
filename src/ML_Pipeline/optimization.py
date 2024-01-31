# define a function for finding optimized budget 

def optimize(budget,coeff_A,ch_names):
    #use pip to install gekko first
    from gekko import GEKKO
    m=GEKKO()
    
    #Assigning lower bound and upper bound to each channel
    x1 = m.Var(lb=100, ub=budget)       
    x2 = m.Var(lb=100, ub=budget)
    x3 = m.Var(lb=100, ub=budget)
    x4 = m.Var(lb=100, ub=budget)
    x5 = m.Var(lb=100, ub=budget)
    lst=[]
    for j in range(5):
        print("Channel",j+1,"should not exceed : ", end='')     #Taking input of upper bound spending on each channel
        z=int(input())
        lst.append(z)
    m.Equation(x1 <= lst[0])
    m.Equation(x2 <= lst[1])
    m.Equation(x3 <= lst[2])
    m.Equation(x4 <= lst[3])
    m.Equation(x5 <= lst[4])
    m.Equation(x1+x2+x3+x4+x5 <= budget)
    m.Maximize(coeff_A[0]*x1 + coeff_A[1]*x2 + coeff_A[2]*x3 + coeff_A[3]*x4 + coeff_A[4]*x5)

    m.solve(disp=False)
    p1 = x1.value[0]
    p2 = x2.value[0]
    p3 = x3.value[0]
    p4 = x4.value[0]
    p5 = x5.value[0]

    #Printing the budget along with the channel names
    print('\n\nBudgets:\n\n')
    print(ch_names[0] + ": " + str(round(p1,0)))
    print(ch_names[1] + ": " + str(round(p2,0)))
    print(ch_names[2] + ": " + str(round(p3,0)))
    print(ch_names[3] + ": " + str(round(p4,0)))
    print(ch_names[4] + ": " + str(round(p5,0)))