num  = 11
if num>1:
    for val in range(2,int(num**0.5)+1):
        if num % val==0:
            print("no prime")
            break
    else:
        print("prime") 
     
