def sq_num(n):
    if n>0:
        sq_num(n-1)
        print(n*n,end=" ")
n=int(input("Enter number :"))
sq_num(n)