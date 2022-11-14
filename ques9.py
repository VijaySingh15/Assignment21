def multiple(n):
    if n>0:
        multiple(n-1)
        print(5*n,end=" ")

n=int(input("Enter number :"))
multiple(n)