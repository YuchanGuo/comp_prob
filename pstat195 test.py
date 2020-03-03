def compute_prob(nTrials,numObserved):
    p=0.5
    comb=0
    a=1
    b=1
    c=1
    for i in range(1,nTrials+1):
        a*=i
    for j in range(1,numObserved+1):
        b*=j
    for l in range(1,nTrials-numObserved+1):
        c*=l
    comb=float(a/(b*c))
    prob=comb*(p**numObserved)*((1-p)**(nTrials-numObserved))
    return prob
