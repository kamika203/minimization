

def f(x):
    return 3*x**2+6*x-1+31*abs(x-4)

def PassMin(N,a,b):
    X=[0 for k in range(N+2)]
    X[0]=a
    X[N+1]=b
    if N%2==0:
        d=(b-a)/(N/2+1)/100
        k=N//2
        for i in range(1,k+1):
            X[2*i]=a+(b-a)/(k+1)*i
            X[2*i-1]=X[2*i]-d
        e=1/2*((b-a)/(N/2+1)+d)
    else:
        for i in range(1,N+1):
            X[i]=a+(b-a)/(N+1)*i
        e=(b-a)/(N+1)
    F=[f(X[i]) for i in range(1,N+1)]
    j=F.index(min(F))+1
    xa=(X[j-1]+X[j+1])/2
    return xa,e



def Fib(N,a,b):
    F=[1,1]
    while(len(F)<N+1):
        F.append(F[-1]+F[-2])
    d=(b-a)/F[N]*0.001
    e=1/2*((b-a)/F[N]+d)
    x1=a+F[N-2]/F[N]*(b-a)
    x2=a+F[N-1]/F[N]*(b-a)
    f1=f(x1)
    f2=f(x2)
    for i in range(N-3):
        if f1<=f2:
            b=x2
            x2=x1
            f2=f1
            x1=a+(b-x1)
            f1=f(x1)
        else:
            a=x1
            x1=x2
            f1=f2
            x2=a+(b-x1)
            f2=f(x2)
    if f1<=f2:
        b=x1
        x2=x1+d
        f2=f(x2)
    else:
        a=x1
        x1=x2
        f1=f2
        x2=x1+d
        f2=f(x2)
    if f1<=f2:
        b=x1
    else:
        a=x1

    xa=(a+b)/2
    return xa,e


a,b=-2,5
N=29 #19%10+20
x=4 #точка минимума
print("Количество вычислений: ",N,"\nТочный ответ: ",x,"\n")

fx,fe=Fib(N,a,b)
px,pe=PassMin(N,a,b)

print("Метод Фибоначи: ",fx,"\nТеоретическая точность:",fe,"\nФактическая точность",abs(fx-x),"\n")
print("Алгоритм пассивного поиска минимума: ", px, "\nТеоретическая точность:",pe,"\nФактическая точность",abs(px-x),"\n")

