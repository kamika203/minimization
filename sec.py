import math

def f(x):
    return x**4/4+2*x**3+4*x**2+4

def pereb(N,a,b,M):
    X=[a+(2*i-1)*(b-a)/(2*N) for i in range(1,N+1)]
    F=[f(X[i]) for i in range(N)]
    e=M*(b-a)/(2*N)
    Fm=min(F)
    return Fm,e

def pokrit(d,a,b,M):
    r=2*d/M
    al=a
    x=[]
    y=[]
    i=0
    while (al<b):
        N = math.ceil((b - al) / r)
        x.append(al + (b - al) / (2 * N))
        y.append(f(x[i]))
        fi = min(y)
        al = x[i] + (y[i] * (fi - d)) / M
        i += 1


    return fi,i



a,b=-5,1
N=29
ft=4
M=15

print("N: ",N,"\nминимальное значение f(x): ",ft,"\n")

per,ep=pereb(N,a,b,M)
print("Метод перебора: ",per,"\nТеоретическая точность:",ep,"\nФактическая точность",abs(per-ft),"\n")

pok,pi=pokrit(ep,a,b,M)
print("Метод покрытия: ",pok,"\nТеоретическая точность:",ep,"\nФактическая точность",abs(pok-ft),"\nКоличество вычислений: ",pi,"\n")
