def odd_rev(n):
    if n>0:
        print(n+(n-1),end=" ")
        odd_rev(n-1)

n=int(input("Enter number :"))
odd_rev(n)