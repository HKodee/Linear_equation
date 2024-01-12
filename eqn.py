from linear import Linear

acox = int(input("enter coefficient of x"))
acoy = int(input("enter coefficient of y"))
aconstant = int(input("enter constnt"))

bcox = int(input("enter coefficient of x"))
bcoy = int(input("enter coefficient of y"))
bconstant = int(input("enter constnt"))

a = Linear(acox,acoy,aconstant)
b = Linear(bcox,bcoy,bconstant)

Linear.__solve__(a,b)
