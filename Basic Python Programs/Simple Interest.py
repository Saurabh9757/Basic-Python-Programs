p=int(input("Enter principle amount: "))
r=int(input("Enter rate of interest: "))
t=int(input("Enter time(in years): "))
SI=p*r*t/100
print("The principle amount is INR {} and the rate of interest is {} % and the time is {} years and its Simple Interest is INR {} .".format(p,r,t,SI))
input()  
