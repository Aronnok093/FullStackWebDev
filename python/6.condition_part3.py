num = int(input("Enter A Number: "))

if(num>0 and num%2==0):
    print("Its A Positive and Even Number")
elif(num>0 and num%2!=0):
    print("Its A Positive and Odd Number")
elif(num<0 and num%2==0):
    print("Its A Negetive and Even Number")
else:
    print("Its A Negetive and Odd Number")
