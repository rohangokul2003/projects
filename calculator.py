"""
Created on Thu Nov  4 10:52:42 2021

@author: rohan gokul

project: calculator
"""

##defing the function
def calculator():
    import math
    print("------------------------------------------------------------------------------------------")
    h='Welcome To Calculator'
    ##printing the heading
    print(h.center(50,'$'))
    
    ##printing the choices
    print("1--> Addition ")
    print("2--> subtraction ")
    print("3--> Multiplication ")
    print("4--> Division ")
    print("5--> Power ")
    print("6--> Square root ")
    print("7--> Percentage ")
    print("8--> Logarithm values ")
    print("9--> Trigonometric values ")
    print("10--> Factorial ")
    
    ##taking the user input of the choice
    choice=int(input("Enter your choice: "))
    
    ##addtion
    if choice==1:
        a=float(input("Enter your first number: "))
        b=float(input("enter your second number: "))
        result=a+b
        print(a,"+",b,"=",result)
    
    ##subtraction
    elif choice==2:
            a=float(input("Enter your first number: "))
            b=float(input("enter your second number: "))
            result=a-b
            print(a,"-",b,"=",result)
    
    ##multiplication        
    elif choice==3:
        a=float(input("Enter your first number: "))
        b=float(input("enter your second number: "))
        result=a*b
        print(a,"x",b,"=",result)

    ##division
    elif choice==4:
        a=float(input("Enter your first number: "))
        b=float(input("enter your second number: "))
        result=a/b
        print(a,"/",b,"=",result)
    
    ##power
    elif choice==5:
        a=float(input("Enter your first number: "))
        b=int(input("enter your second number: "))
        result=pow(a,b)
        print(a,"power of",b,"=",result)
    
    ##square root
    elif choice==6:
        a=int(input("Enter your number: "))
        result=math.sqrt(a)
        print("sqrt(",a,") =",result)
    
    ##percentage
    elif choice==7:
        a=float(input("Enter your first number: "))
        b=int(input("enter your second number: "))
        d=b/a
        p=d*100
        if a>b:
            print("percentage=",p)
        else:
            print("invalid inputs")
    
    ##log values
    elif choice==8:
        x=int(input("enter a number:"))
        result=math.log( x )
        print("log(",x,") = ",result)
    
    ##trigonometric values
    elif choice==9:
        print("1--> sin")
        print("2--> cos")
        print("3--> tan")
        print("4--> cot")
        print("5--> secant")
        print("6--> cosecant")
        choice=int(input("enter your choice: "))
        if choice==1:
            x=int(input("enter your value:"))
            result=math.sin(math.radians(x))
            print(result)
        elif choice==2:
            x=int(input("enter your value:"))
            result=math.cos(math.radians(x))
            print(result)
        elif choice==3:
            x=int(input("enter your value:"))
            result=math.tan(math.radians(x))
            print(result)
        elif choice==4:
            x=int(input("enter your value:"))
            result=math.cot(math.radians(x))
            print(result)
        elif choice==5:
            x=int(input("enter your value:"))
            result=math.secant(math.radians(x))
            print(result)
        elif choice==6:
            x=int(input("enter your value:"))
            result=math.cosecant(math.radians(x))
            print(result)
        else:
            print("invalid input")
    ##factorial
    elif choice==10:
        a=int(input("enter the number: "))
        result=math.factorial(a)
        print("factorial of",a,"is",result)

    else:
        print("invalid input")
                
    ## asking did you want to continue            
    again=int(input("do you want to calculate again (1/0) : "))
    
    if again==1:
              ##function calling
              calculator()
              print("------------------------------------------------------------------------------------------")
    else:
                 ##ending the program
                 h='thanks for using me'
                 print(h.center(50,'$'))
                 print("------------------------------------------------------------------------------------------")
    
##starting and calling the function    
calculator()
                        
                        

    
    


