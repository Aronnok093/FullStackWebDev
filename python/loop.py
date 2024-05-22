def multiplication(n):
    for i in range(1,11):
        print("{} X {} = {}".format(i,n,n*i))
    print("")

multiplication(3)

num=int(input("Enter Range: "))
i=1
while i<=num:
    multiplication(i)
    i+=1