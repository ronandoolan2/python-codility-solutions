def most_common(X):
    maxcount = 0
    uniqX = list(set(X))
    for x in uniqX:
        if X.count(x) > len(X)/2:
            return x
            #most_common = x
            #maxcount = X.count(x)
    #return most_common

def check_common(X, j):
    #maxcount = 0
    #uniqX = list(set(X))
    if X.count(j) > len(X)/2:
        return True
    else:
        return False

def solution(A):
    # write your code in Python 2.7
    equi_leaders = 0
    most_common_A = most_common(A)
    lcount = 0
    rcount = A.count(most_common_A)
    for i in range(0, len(A)):
        if A[i] == most_common_A:
            lcount += 1
            rcount -= 1
            if i+1 < lcount*2:
                if len(A) - (i+1) < rcount*2:
                    #print len(A) - (i+1)
                    equi_leaders += 1
                    #print i
                    
    #for i in range(1, len(A)):
    #   if check_common(A[:i], most_common_A) == True: 
    #      if check_common(A[i:], most_common_A) == True:
    #         equi_leaders += 1
    return equi_leaders
