n=int(input("enter a number ="))
if n<0:
    print("plz enter non negative numbers only")
elif n==0:
    print("factorial of 0 is 1")
elif n>0:
    x=1
    fact=1
    while x<=n:
        fact*=x
        x+=1
    print("fact of n is ",fact)