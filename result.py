#result
sno=int(input("enter the num: "))
sname=input("enter the name: ")
sgroup=input("enter the group: ")
s1=int(input("enter the s1 marks: "))
s2=int(input("enter the s2 marks: "))
s3=int(input("enter the s3 marks: "))
total=s1+s2+s3
avg=total/3
print("total:",total)
print("average",avg)
if avg>=90:
    print("o grade")
elif avg>=80:
    print(" A grade")
elif avg>=70:
    print("B grade")
elif avg>=60:
    print("C grade")
elif avg>=50:
    print("D grade")
else:
    print("pass")
