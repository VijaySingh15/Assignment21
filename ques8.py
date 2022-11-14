def cube_num(n):
    if n>0:
        cube_num(n-1)
        print(n**3,end=" ")
n=int(input("Enter number :"))
cube_num(n)