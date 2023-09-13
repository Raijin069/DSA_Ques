def count(n):
    score = [0 for _ in range(n+1)]
    
    score[0] = 1
    
    for i in range(3,n+1):
        score[i]+=score[i-3]
    
    for i in range(5,n+1):
        score[i]+=score[i-5]
    
    for i in range(10,n+1):
        score[i]+=score[i-10]
        
    return score[n]