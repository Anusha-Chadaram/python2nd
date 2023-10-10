#emi calculation
p=int(input("enter the principal value:"))
t=int(input("enter the time value :"))
r=int(input("enter the rate value:"))
si=p*t*r/100
emi=(si+p)/(12*t)
print("the emi value is:",emi)
     
