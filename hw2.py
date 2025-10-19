#answer for question 1

def BFS(TREE):
    res=tuple()
    x=tuple()
    for t in TREE:
        if type(t)!=tuple:
            res+=(t,)
        else:
            x+=t
    if len(x)>0:
        res+=BFS(x)
    return res

# test cases for question 1

# print(BFS(((("L", "E"), "F"), "T")))
# print(BFS(("R", ("I", ("G", ("H", "T"))))))
# print(BFS((("A", ("B",)), ("C",), "D")))
# print(BFS(("T", ("H", "R", "E"), "E")))
# print(BFS(("A", (("C", (("E",), "D")), "B"))))
#------------------------------------------------

#answer for question 2

def DFS(TREE):
    res=tuple()
    for t in TREE:
        if type(t)!=tuple:
            res+=(t,)
        else:
            res+=DFS(t)
    return res

#test cases for question 2

# print(DFS(((("L", "E"), "F"), "T")))
# print(DFS(("R", ("I", ("G", ("H", "T"))))))
# print(DFS((("A", ("B",)), ("C",), "D")))
# print(DFS(("T", ("H", "R", "E"), "E")))
# print(DFS(("A", (("C", (("E",), "D")), "B"))))
#------------------------------------------------

#answer for question 3

def DFID(TREE,D):
    result=tuple()
    
    def BFS_DFID(tree,d):
        res=tuple()
        x=tuple()
        for t in tree:
            if type(t)==tuple and d-1>=0:
                res+=(BFS_DFID(t,d-1),)
            elif type(t)!=tuple:
                res+=(t,)
        return res
    
    def DFS_DFID(tree):
        res=tuple()
        for t in tree[::-1]:
            if type(t)!=tuple:
                res+=(t,)
            else:
                res+=DFS_DFID(t)
        return res
     
    for d in range(D):
        result+=(DFS_DFID(BFS_DFID(TREE,d)))
    return result

#test cases for question 3

# print(DFID(((("L", "E"), "F"), "T"), 3))
# print(DFID(("R", ("I", ("G", ("H", "T")))), 4))
# print(DFID(((("A", ("B",)), ("C",), "D")), 3))
# print(DFID(("T", ("H", "R", "E"), "E"), 2))
# print(DFID(("A", (("C", (("E",), "D")), "B")), 5))
#------------------------------------------------

#answer for question 4

def FINAL_STATE(S):
    return S==(True,True,True,True)

def NEXT_STATE(S, A):
    S=list(S)
    if A=='h':
        S[0]=not(S[0])
    elif A=='b' and S[0]==S[1]:
        S[0],S[1]=not(S[0]),not(S[1])
    elif A=='d' and S[0]==S[2]:
        S[0],S[2]=not(S[0]),not(S[2])
    elif A=='p' and S[0]==S[3]:
        S[0],S[3]=not(S[0]),not(S[3])
    else:
        return []
    if (S[1]==S[2] and S[0]!=S[1]) or (S[1]==S[3] and S[0]!=S[1]):
        return []
    else:
        return tuple(S)

def SUCC_FN(S):
    states=[]
    for A in ['h','b','d','p']:
        next_state=NEXT_STATE(S,A)
        if next_state!=[]:
            states.append(next_state)
    return states

def ON_PATH(S, STATES):
    return S in STATES

def MULT_DFS(STATES, PATH):
    for s in STATES:
        if FINAL_STATE(s):
            PATH.append(s)
            return PATH
        elif ON_PATH(s,PATH):
            continue
        else:
            PATH.append(s)
            MULT_DFS(SUCC_FN(s),PATH)
    return []
            
def DFS_SOL(S, PATH):
    if ON_PATH(S,PATH):
        return []
    else:
        PATH.append(S)
    if FINAL_STATE(S):
        return PATH
    succ_states=SUCC_FN(S)
    return MULT_DFS(succ_states,PATH)

#testing for question 4

# print(DFS_SOL((False,False,False,False),[]))
