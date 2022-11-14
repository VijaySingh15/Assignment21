def reverse(n,r):
    if n==0:
        return r
    else:
        return reverse(n//10,r*10 + n%10)

num=int(input("Enter number :"))
reversed_num=reverse(num,0)
print("Reverse of %d is %d"%(num,reversed_num))