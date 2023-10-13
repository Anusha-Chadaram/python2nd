#shopping bill
frock=1500
geans=1000
chudi=2500
shirt=3000
cname=input("enter customer name")
cphno=input("enter the customer phone number")
nfrock=int(input("enter no of frocks :"))
ngeans=int(input("enter no. of geans :"))
nchudi=int(input("enter the no of chudi :"))
nshirt=int(input("enter the no of shirt :"))
bill=(frock*nfrock)+(geans*ngeans)+(chudi*nchudi)+(shirt*nshirt)
if bill>=8000:
    dis=bill*80/100
elif bill>=7000:
    dis=bill*70/100
elif bill>6000:
    dis=bill*60/100
elif bill>=5000:
    dis=bill*50/100
elif bill>=4000:
    dis=bill*40/100
elif bill>=3000:
    dis=bill*30/100
elif bill>=2000:
    dis=bill*20/100
elif bill>=1000:
    dis=bill*10/100
else:
    dis=0
price=bill-dis
gst=price*12/100
amount=price+gst
print("bill to be paid",amount)
print("tq")

