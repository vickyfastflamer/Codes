def toh(n,from_,to_,aux):
    if n==1:
        print('disk ',n,'is moved from',from_,'to',to_ )
        return
    toh(n-1,from_,aux,to_)
    print('disk ',n,'is moved from',from_,'to',to_)
    toh(n-1,aux,to_,from_)

toh(3,"A","B","C")