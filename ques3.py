def odd_natural(n):
    if n>0:
        odd_natural(n-1)
        print(n+(n-1),end=" ")

n=int(input("Enter number :"))
odd_natural(n)