a = 100000000
for m in range(1,9):
    if(m>=1 and m<=2):
        b=a*0
        print("laba bulan ke-",m," : ",b)
    if(m>3 and m<=4):
        c=a*0.1
        print("Laba bulan ke-",m," : ",c)
    if(m>5 and m<=7):
        d =a*0.5
        print("Laba bulan ke-",m," : ",d)
    if(m==8):
        e=a*0.2
        print("Laba bulan ke-",m," : ",e)
total = b+b+c+c+d+d+d+e
print("\nTotal : ",total)
