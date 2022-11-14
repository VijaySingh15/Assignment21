def even_num(n):
    if n>0:
        even_num(n-1)
        print(2*n,end=" ")

n=int(input("Enter number :"))
even_num(n)