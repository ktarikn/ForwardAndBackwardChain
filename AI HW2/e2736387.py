import re
from itertools import count

FAIL = None
##how I get and run the command
given = []
inp = input()
while(inp !=")"):
    given.append(inp)
    inp = input()
given.append(inp)
command = "".join(given)
#eval(command) in the end

def apply_mgu(unifier:list, text:str): #seemingly done, although maybe not optimal, update: WORKS!
    p1 = r"[\(, ]"
    p2 = r"[\), ]"
    for uni in unifier:
        if(uni == ()):
            continue
        if(text == uni[0]):
            return uni[0]
        reguni = p1+uni[0]+p2
        if(re.search(reguni,text)): #so we don't turn Example(x) to  EAliceample(Alice)
            matc = re.search(reguni,text)
            text = text[0:matc.start()+1] + uni[1] + text[matc.end()-1:]
    return text
        

def mgu(E1:str,E2:str): #seemingly done
    print("E1:" + E1 + "\nE2:"+E2)
    if(E1.__contains__(" ") and E2.__contains__(" ")): #not atomic  
        E1 = E1.strip("()")
        E2 = E2.strip("()")
        indexE1 = E1.index(" ")
        indexE2 = E2.index(" ")
        Z1:list = mgu(E1[0:indexE1],E2[0:indexE2])
        if(Z1 == FAIL):
            return FAIL
        T1 = E1[indexE1+1:]# text remaining after first element
        T2 = E2[indexE2+1:]
        G1 = apply_mgu(Z1,T1)
        G2 = apply_mgu(Z1,T2)
        Z2 = mgu(G1,G2)
        if(Z2 == FAIL):
            return FAIL
        Z1.extend(Z2)
        return Z1 #Z1oZ2

    
    #assuming variables are lowercase letters
    elif(E1.__len__() == 1 and E1.islower()): #E1 is a variable
        p1 = r"[\(, ]"
        p2 = r"[\), ]"
        if(re.search(p1+E1+p2,E2)):
            return FAIL
        return [(E1,E2)]
        

    elif(E2.__len__() == 1 and E2.islower()):
        p1 = r"[\(, ]"
        p2 = r"[\), ]"
        if(re.search(p1+E2+p2,E1)):
            return FAIL
        return [(E2,E1)]

    else:
        if(E1 == E2):
            return [()]
        return FAIL
    
#TODO turn Example(x,y) to (Example x y) or make mgu accept it as is

eval(command) #run at your own risk I guess :p