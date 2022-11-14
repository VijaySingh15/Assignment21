def natural_num(n):
    if n>0:
        natural_num(n-1)
        print(n,end=" ")

n=int(input("Enter number :"))
natural_num(n)