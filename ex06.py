n = int(input("請輸入一個整數值，並出可以除多少次？"))
k=0
while (n%2==0):
    k+=1    #n= 120/2
    n=n/2
    print(n,"是第", format(k),"次")
    
