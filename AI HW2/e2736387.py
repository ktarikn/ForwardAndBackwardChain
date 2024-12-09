import re
from itertools import count

FAIL = None
##how I get and run the command
given = []
inp = input()
while(inp !=")"):
    given.append(inp)
    inp = input

command = "".join(given)

eval(command)
def apply_mgu(unifier, text):
    pass
def mgu(E1:str,E2:str):
    if(E1.__contains__(" ") and E2.__contains__(" ")): #not atomic  
        E1 = E1.strip("()")
        E2 = E2.strip("()")
        indexE1 = E1.index(" ")
        indexE2 = E2.index(" ")
        Z1:list = mgu(E1[0:indexE1],E2[0:indexE2])
        if(Z1 == FAIL):
            return FAIL
        T1 = E1[indexE1+1:-1]# text remaining after first element
        T2 = E2[indexE2+1:-1]
        G1 = apply_mgu(Z1,T1)
        G2 = apply_mgu(Z1,T2)
        Z2 = mgu(G1,G2)
        if(Z2 == FAIL):
            return FAIL
        Z1.extend(Z2)
        return Z1

    #assuming variables are lowercase letters
    elif(E1.__len__() == 1 and E1.islower()): #E1 is a variable
        if(E1 == E2):
            return [{}]
        

    elif(E2.__len__() == 1 and E2.islower()):
        pass