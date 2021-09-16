#Joseph Wehbe - Exercise 3

def Hundreds(n):
    t=n//100
    return (Ones(t))


def Tens(n):
    t=n//10
    return(Ones(t))


def Ones(n):
    y=n%10
    return y


def Cubed(n):
    return(n**3)

def isArmestrong(n):
    k=0
    if n==(Cubed(Ones(n))+Cubed(Tens(n))+Cubed(Hundreds(n))):
           k=1
    return k

#This function will show the armestrong integers 

def NbArmestrong():
    a=int(input("Enter The First Number= "))
    b=int(input("Enter The Second Number= "))
    i=a
    d=0
    while i<=b:
        if isArmestrong(i)==1:
        # d=d+1
         print(i)
        i=i+1
    #print("The number of Armestrong Integers displayed is:",d)

NbArmestrong()
