from time import time

def generadores(n):
    s = set(range(1, n))
    print('S: ', s)
    r = []
    for a in s:
        g = set()
        for x in s:
            g.add((a**x) % n)
        if g == s:
            r.append(a)
    return r

def DLP():

    n = int(input("Valor de Z: "))
    gndrs = generadores(n)

    if(len(gndrs)!=0):
        print('Finito ciclico')
    else:
        print('No finito ciclico')
    if gndrs:
        print(f"Z_{n} Generadores {gndrs}")
    grupo=range(1,n)
    for x in gndrs:

        for i in grupo:
            res= (x**i)%n
            print(x,"^",i,"mod",n,"=",res)
        print("------------")
start_time = time()
DLP()
elapsed_time= time() - start_time
print(elapsed_time)