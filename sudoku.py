import sympy as sp
import math
import json

def all(k):
    '''
    Args:
    k: int
    
    Returns:
    list of solutions of (k^2,k^2)
    '''
    n = k*k
    X = [sp.var('x'+ str(i)) for i in range(1,n*n + 1)]
    P1 = [(math.prod((X[v] - i) for i in range(1,n+1))) for v in range(n*n)]
    
    def delta(x,j):
        # returns 1 if x = j, 0 otherwise
        num = math.prod((x - i) for i in range(1,n + 1) if i != j)
        deno = num.subs(x,j)
        return num/deno
    
    P2 = []
    for i in range(n*n):
        for j in range(i+1,n*n):
            r1,c1 = i//n, i%n
            r2,c2 = j//n, j%n
            if r1 == r2 or c1 == c2 or (r1//k == r2//k and c1//k == c2//k):
                p = 0
                for a in range(1,n + 1):
                    for b in range(1,n + 1):
                        if a != b:
                            p += (delta(X[i],a)*delta(X[j],b))
                P2.append(p - 1)

    P = P1 + P2
    result = sp.groebner(P,*X, order='lex')
    return sp.solve(result, *X)

def solve(sudoku):
    '''
    Args:
    sudoku: list of lists
    
    Here, the sudoku is a list of lists of integers.
    The integers are the values of the sudoku.
    The empty cells are denoted by 0.
    
    Returns:
    list of solutions
    '''

    n = len(sudoku)
    k = int(math.sqrt(n))
    X = [sp.var('x'+ str(i)) for i in range(1,n*n + 1)]
    P1 = [(math.prod((X[v] - i) for i in range(1,n+1))) for v in range(n*n)]
    
    def delta(x,j):
        # returns 1 if x = j, 0 otherwise
        num = math.prod((x - i) for i in range(1,n + 1) if i != j)
        deno = num.subs(x,j)
        return num/deno
    
    P2 = []
    for i in range(n*n):
        for j in range(i+1,n*n):
            r1,c1 = i//n, i%n
            r2,c2 = j//n, j%n
            if r1 == r2 or c1 == c2 or (r1//k == r2//k and c1//k == c2//k):
                p = 0
                for a in range(1,n + 1):
                    for b in range(1,n + 1):
                        if a != b:
                            p += (delta(X[i],a)*delta(X[j],b))
                P2.append(p - 1)

    P3 = [] # for values already in given sudoku
    for i in range(n*n):
        if sudoku[i//n][i%n] != 0:
            P3.append(X[i] - sudoku[i//n][i%n])
    
    P = P1 + P2 + P3    
    json.dump(str(P),open('P.json','w'))
    result = sp.groebner(P,*X, order='lex')
    print(result)
    return sp.solve(result, *X)

# sol = solve([
#     [0,0,4,3],
#     [0,0,0,0],
#     [0,0,0,0],
#     [2,3,0,0]
#     ])

sol = all(2)
print(len(sol))
json.dump(str(sol),open('solutions.json','w'))