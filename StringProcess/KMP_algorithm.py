def kmp(mom_string, son_string):
    m = s = 0
    nex = getNext(p)
    while s < len(son_string) and m < len(mom_string):
        if s == -1 or mom_string[m] == son_string[s]:
            s += 1
            m += 1
        else:
            s = nex[s]
    if s == len(son_string):
        return m - s
    else:
        return -1  

def getNext(p):
    nex = [0] * len(p)
    nex[0] = -1

    i = 0
    j = -1
    while (i < len(p) - 1):
        if j == -1 or p[i] == p[j]:
            i += 1
            j += 1
            nex[i] = j
        else:
            j = nex[j]
    
    return nex

s = 'ababababca'
p = 'abababc'
print(getNext(p))
print(kmp(s,p))