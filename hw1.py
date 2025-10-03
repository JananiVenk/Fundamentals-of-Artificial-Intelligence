# Answer for Question 1

def PAD(N):
    if N==0 or N==1 or N==2:
        return 1
    else:
        return PAD(N-2)+PAD(N-3)
    
# Testing for Question 1

# for i in range(15):
#     print(PAD(i))

# --------------------------


# Answer for Question 2

def SUMS(N):
    if N==0 or N==1 or N==2:
        return 0
    else:
        return SUMS(N-2)+SUMS(N-3)+1

# testing for Question 2

# for i in range(10):
#     print(SUMS(i))

# --------------------------


# Answer for Question 3

def ANON(TREE):
    if type(TREE)!=tuple:
        return '?'
    else:
        return tuple(ANON(t) for t in TREE)

# Testing for Question 3

# print(ANON(42))
# print(ANON("FOO"))
# print(ANON(((("L", "E"), "F"), "T")))
# print(ANON((5, "FOO", 3.1, -0.2)))
# print(ANON((1, ("FOO", 3.1), -0.2)))
# print(ANON((((1, 2), ("FOO", 3.1)), ("BAR", -0.2))))
# print(ANON(("R", ("I", ("G", ("H", "T"))))))

# --------------------------


# Answer for Question 4

def TREE_HEIGHT(TREE):
    if type(TREE)!=tuple:
        return 0
    else:
         return 1+max([TREE_HEIGHT(t) for t in TREE])

# testing for Question 4

# print(TREE_HEIGHT(1))
# print(TREE_HEIGHT((5, "FOO", 3.1, -0.2)))
# print(TREE_HEIGHT((1, ("FOO", 3.1), -0.2)))
# print(TREE_HEIGHT(("R", ("I", ("G", ("H", "T"))))))

# --------------------------


# Answer for Question 5

def TREE_ORDER(TREE):
    if type(TREE)!=tuple:
        return (TREE,)
    else:
        return TREE_ORDER(TREE[0])+TREE_ORDER(TREE[2])+TREE_ORDER(TREE[1])

# testing for Question 5

# print(TREE_ORDER(42))
# print(TREE_ORDER(((1, 2, 3), 7, 8)))
# print(TREE_ORDER(((3, 7, 10), 15, ((16, 18, 20), 30, 100))))

# --------------------------
# --------------------------