def rev_even(n):
    if n>0:
        print(2*n,end=" ")
        rev_even(n-1)    
    
n=int(input("Enter number :"))
rev_even(n)