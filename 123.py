import time
import os
def getdot(val):
    a=['','.','..','...']
    return a[val]
while True:
    l=0
    while l<4:
        os.system('title Loding %s'%(getdot(l)))
        os.system('cls')
        print('\n\n\n\n\t\t\tLoading%s'%(getdot(l)))
        l+=1
        time.sleep(1)