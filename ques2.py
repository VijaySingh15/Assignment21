def rev_natural(n):
    if n>0:
        print(n,end=" ")
        rev_natural(n-1)


n=int(input("Enter number :"))
rev_natural(n)