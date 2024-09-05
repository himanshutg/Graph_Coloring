import sympy as sp

def solve(numVariables, clauses):
    '''
    Args:
    numVariables: int
    clauses: list of tuples
    
    The tuples are the clauses of the k-SAT problem.
    Each element of the tuple is a variable.
    i => xi
    -i => xi^c
    (1,2,...n) => (x1,x2,....xn)
    (-1,-2,...-n) => (x1^c,x2^c,...xn^c) 
        
    Returns:
    list of solutions
    '''
    X = [sp.var('x'+ str(i)) for i in range(1,numVariables + 1)]
    P1 = [xi*(xi - 1) for xi in X]
    P2 = []
    for clause in clauses:
        p = math.prod((X[v-1] - 1) if v > 0 else X[-v-1] for v in clause)
        P2.append(p)
    P = P1 + P2
    
    result = sp.groebner(P,*X, order='lex')
    return sp.solve(result, *X)