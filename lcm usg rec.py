def lcm(n1,n2,t):
    if t>n1 or t>n2 :
        return n1*n2
    if n1%t==0 and n2%t==0:  
        n1=n1//t
        n2=n2//t
        return t*lcm(n1,n2,t)
    else:
        return lcm(n1,n2,t+1)
    
