from colorama import Fore,Back,Style,init
import os
init()
os.system("cls" or "clear")

def top(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==n or (j<=i and i+j>=n+1):
                print(Back.RED,end="  "+Style.RESET_ALL)
            else:
                print(Back.BLUE,end="  "+Style.RESET_ALL)
        print()
    

def middle(n):
    for i in range(1,n+1):  
        for j in range(1,n+1):
            if (j==2 and i==1) or (i==1 and j==n-1) or (i==n-1 and j==n-1):
                print(Fore.YELLOW+Back.MAGENTA,end=" #"+Style.RESET_ALL)   
            elif (i==n or i==n-1) and j==int(n/2)+1:
                print(Fore.BLACK+Back.LIGHTRED_EX,end="||"+Style.RESET_ALL) 
            else:
                print(Back.WHITE,end="  ")
        print()
        
def ground(n):
    for i in range(1,n-1):
        print(end=f"{Back.LIGHTGREEN_EX}  {Back.GREEN}  ")
    print(Style.RESET_ALL)

while True:
    print(Style.RESET_ALL)
    n=int(input("Please Enter a number greater than 4 (to exit enter -1): "))
    if n==-1:
        break
    elif n<5:
        print("Wrong number! 5 or more")
    else:
        top(n)
        middle(n)
        ground(n)
            
