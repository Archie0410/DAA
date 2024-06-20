def the_factors(n):
    fact=[]
    for i in range(1,n+1):
        if n%i==0:
            fact.append(i)
    return fact
    
num=int(input("Enter a number:"))
if num>0:
    factors=the_factors(num)
    print("The factors of",num,"are",factors)
else:
    print("Enter a positive number")
