import math
import random
#weight functions for different methods
def midpoint_wt(n):
    return(1)

def trapezoid_wt(n,N):
    if n==N or n==0:
        return(1/2)
    else:
        return(1)

def simpson_wt(n,N):
    if n==0 or n==N:
        return(1/3)
    elif n%2==0 and n!=N:
        return(2/3)
    elif n%2==1 and n!=N:
        return(4/3)

def num_int(f,a,b,N,method):
    '''
    Numerical integration
    ----------------------
    input: function, lower limit, upper limit, number of intervals, method of evaluation

    output: result of the integration

    '''
    h=(b-a)/N
    if method=='midpoint':
        sum=0
        for i in range(1,N+1):
            sum+=f(a+(2*i-1)*h/2)*midpoint_wt(i)*h
        return(sum)
    elif method=='trapezoidal':
        sum=0
        for i in range(N+1):
            sum+=f(a+i*h)*trapezoid_wt(i,N)*h
        return(sum)
    elif method=='simpson':
        sum=0
        for i in range(N+1):
            sum+=f(a+i*h)*simpson_wt(i,N)*h
        return(sum)

def MonteCarloInt(f,a,b,N):
    """
    Monte Carlo Integration
    ---------------------------
    input: function, a, b, number of random numbers in the interval [a,b]

    output:result of the integration
    
    """
    f_X=[f(random.uniform(a,b)) for _ in range(N)]
    f_X2=[i**2 for i in f_X]
    F_n=(b-a)*sum(f_X)/N
    stdev=math.sqrt(sum(f_X2)/N - (F_n/(b-a))**2)*(b-a)
    return(F_n,stdev,f_X)