def dol(a):
    x = a * 84.58
    print(x)
    
def eur(a):
    x = a * 95.76
    print(x)
    
def pound(a):
    x = a * 112.38
    print(x)
    
def dhir(a):
    x = a * 23.01
    print(x)
    
    
print("Hi! what which currency would you like to convert to inr?")
print("1. dollar")
print("2. euro")
print("3. pound")
print("4. dhiram")

while True:
    z = input("for process1/2/3/4: ")
    
    if z in ("1", "2", "3", "4"):
        try:
            x = int(input("Enter the number which you want to be converted: "))
            
        except ValueError:
            print("Invalid format please try again")
            
    if(z=="1"):
        dol(x)
        
    elif(z=="2"):
        eur(x)
        
    elif(z=="3"):
        pound(x)
        
    elif(z=="4"):
        dhir(x)
        
        
    c = input("Would you like to do it again? (y/n): ")
    
    if(c=="y"):
        continue
    
    elif(c=="n"):
        print("Session concluded. Executed with code 0")
        break